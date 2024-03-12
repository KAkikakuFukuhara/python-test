import pyrealsense2 as rs
import math
import numpy as np

def is_in_range(limit_high :int, x: int) -> bool:
    return 0 <= x < limit_high

def get_meter_from_depthframe(depth_frame: rs.depth_frame, x :int, y :int) -> list:
    """
    Args:
     depth_frame:
      rs.depth_frame
     x: int
      width_postion on pixel
     y: int
      height_postion on pixel
    """
    frame_width = depth_frame.get_width()
    frame_height = depth_frame.get_height()
    if not is_in_range(frame_width, x):
        raise Exception(" over range in frame_width ")
    if not is_in_range(frame_height, y):
        raise Exception(" over range in frame_height ")
    
    depth_intrin = depth_frame.profile.as_video_stream_profile().intrinsics
    depth = depth_frame.get_distance(x, y)
    # 指定ピクセルの（横、高さ、深さ）meterの取得
    point = rs.rs2_deproject_pixel_to_point(depth_intrin, [x, y], depth)

    return point

class CameraWithIMU:
    def __init__(self):
        # camera parameter
        self.streaming_flag = False
        
        # frame parameter
        self.frames = None

        # camera angle paramter
        self.first  = True
        self.thetaX = None
        self.thetaY = None
        self.thetaZ = None
        self.alpha = 0.98
        
        # camera pipeline configure
        self.p = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.accel)
        config.enable_stream(rs.stream.gyro)
        self.config = config
        align_to = rs.stream.color
        self.align = rs.align(align_to)

    def start(self):
        # カメラ起動中のスタートは無効
        assert not self.is_streaming(), \
            ("既にカメラは起動中です。２回目の起動は認めていません")

        try:
            self.p.start(self.config)
            self.streaming_flag = True
            print("Camera Start !!")
            self.update_frames()
        except Exception as e:
            raise e
        
    def stop(self):
        if self.is_streaming():
            try:
                self.p.stop()
                self.first = True
                self.streaming_flag = False
                print("Camera Stop !!")
            except Exception as e:
                raise e
        else:
            print("カメラは起動していません")
                
    def is_streaming(self):
        return self.streaming_flag
            
    def update_frames(self):
        assert self.is_streaming()
        org_frames  = self.p.wait_for_frames()
        self.frames = self.align.process(org_frames)
        self.calc_angles()

    def get_frames(self):
        assert self.is_streaming()
        return self.frames

    def get_color_frame(self):
        frames = self.get_frames()
        return frames.get_color_frame()

    def get_color_image(self):
        color_frame = self.get_color_frame()
        return np.asanyarray(color_frame.get_data())

    def get_depth_frame(self):
        frames = self.get_frames()
        return frames.get_depth_frame()

    def get_image_frames(self):
        frames = self.get_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if (color_frame is None) or (depth_frame is None):
            self.stop()
            raise Exception("Camera Coudn't get ColorFrame or DepthFrame")

        return color_frame, depth_frame

    def calc_angles(self):
        
        # get composite_frame(color, depth, accel, gyro) form RealSense D435i
        frames = self.get_frames()
        
        # get_imu_data  
        for frame in frames:
            name = frame.get_profile().stream_name()
            if name == "Gyro":
                gyro = frame.as_motion_frame().get_motion_data()
                ts = frames.get_timestamp()
            elif name == "Accel":
                accel = frame.as_motion_frame().get_motion_data()
            
        #convert parameters
        accel_x =   accel.z
        accel_y = - accel.x
        accel_z = - accel.y

        gyro_x =   gyro.z
        gyro_y = - gyro.x
        gyro_z = - gyro.y

        #calculation for the first frame
        if self.first:
            self.first = False
            self.last_ts_gyro = ts
                
            # accelerometer calculation
            accel_angle_x = math.atan2(accel_y, accel_z)
            accel_angle_y = math.atan2(-accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2))
            accel_angle_z = 0

            # setting init theta
            self.thetaX = accel_angle_x
            self.thetaY = accel_angle_y
            self.thetaZ = accel_angle_z
            return
        
        #calculation for the second frame onwards
      
        # gyrometer calculations
        dt_gyro = (ts - self.last_ts_gyro) / 1000.0
        self.last_ts_gyro = ts

        gyro_angle_x = gyro_x * dt_gyro
        gyro_angle_y = gyro_y * dt_gyro
        gyro_angle_z = gyro_z * dt_gyro

        thetaX = self.thetaX + gyro_angle_x
        thetaY = self.thetaY + gyro_angle_y
        thetaZ = self.thetaZ + gyro_angle_z

        #accelerometer calculation
        accel_angle_x = math.atan2(accel_y, accel_z)
        accel_angle_y = math.atan2(-accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2))

        alpha = self.alpha
        #combining gyrometer and accelerometer angles
        self.thetaX = thetaX * alpha + accel_angle_x * (1-alpha)
        self.thetaY = thetaY * alpha + accel_angle_y * (1-alpha)
        self.thetaZ = thetaZ

        return
        
    def get_camera_angles(self):
        assert self.is_streaming(), ("Camera is not streaming")
        roll  = math.degrees(self.thetaX)
        pitch = math.degrees(self.thetaY)
        yaw   = math.degrees(self.thetaZ)
        return roll, pitch, yaw