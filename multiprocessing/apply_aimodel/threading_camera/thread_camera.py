""" Threadで用いることができるカメラオブジェクト
"""
import math
import time
from threading import Thread, Lock
from queue import Queue, Full
from typing import Optional, Tuple

import numpy as np
import pyrealsense2 as rs

###############################
# begin "class ThreadCamera"
###############################
class ThreadCamera(Thread):
    """ 
    概要:
        Threadを継承したカメラ
    
    """
    def __init__(self, output:Queue)-> None:
        super().__init__()

        # camera parameter
        self.streaming_flag : bool = False

        # thread config
        self.output : Queue = output
        self.exit_flag : bool = False
        self.stop_flag : bool = False
        self.lock = Lock()
        
        # frame parameter
        self.frames : Optional[rs.composite_frame] = None
        self.start_time : Optional[float] = None
        self.elapsed_time : Optional[float] = None
        # camera angle paramter
        self.first : bool = True
        self.thetaX : Optional[float] = None
        self.thetaY : Optional[float] = None
        self.thetaZ : Optional[float] = None
        self.alpha : float = 0.98

        # camera pipeline configure
        self.p = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.accel)
        config.enable_stream(rs.stream.gyro)
        self.config : rs.config = config
        align_to = rs.stream.color
        self.align = rs.align(align_to)

    def p_start(self):
        """ start camera(pipeline)
        """
        print("[Info type=Camera] Start Capture")
        self.p.start(self.config)

    def p_stop(self):
        """ stop camera(pipeline)
        """
        print("[Info type=Camera] Stop Capture")
        self.p.stop()

    def update(self):
        """ update frame and camera angles
        """
        self.frames = self.p.wait_for_frames()
        
        #calc_angle_start_time = time.time()
        self.calc_camera_angles()
        #calc_angle_finsh_time = time.time()
        #elapsed_time = calc_angle_finsh_time - calc_angle_start_time
        #print(f"Elapsed Time (calc_angles):{elapsed_time:.8f}")

    def calc_camera_angles(self) -> None:
        """ calculate camera_angles from gyro and acclel cencer 
        """
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
        
        # end "def calc_camera_angles"

    def make_queue_data(self) -> tuple:
        """ make queue data
        """
        c_r = math.degrees(self.thetaX)
        c_p = math.degrees(self.thetaY)
        c_y = math.degrees(self.thetaZ)
        angles = (c_r, c_p, c_y)
        color_frame = self.frames.get_color_frame()
        depth_frame = self.frames.get_depth_frame()
        queue_data = (angles, color_frame, depth_frame)
        return queue_data

    def get_frames(self) -> rs.composite_frame:
        """ 更新したフレームを取得する
        """
        return self.frames

    def set_exit_flag(self):
        """ set exit_flag from other thread
        """
        with self.lock:
            self.exit_flag = True


    def set_stop_flag(self):
        """ set stop_flag from other thread
        """
        with self.lock:
            self.stop_flag = True
    
    def run(self) -> None:
        """ ovarload Thrad.run
        """
        try:
            self.p_start()
        except Exception as e:
            print("[Exception: Type=Camera] pipe can't start")
            print(e)
            return

        try:
            while True:
                with self.lock:
                    exit_flag = self.exit_flag
                    stop_flag = self.stop_flag

                if exit_flag:
                    break
                
                self.update()
                
                if not stop_flag:
                    queue_data = self.make_queue_data()
                    try:
                        self.output.put_nowait(queue_data)
                    except Full:
                        self.output.get()
                        self.output.put_nowait(queue_data)
        finally:
            self.p_stop()
            print("[Info type=System] Exit Thread camera")
        
        # end "ThreadCamera.run"

# end "class ThreadCamera"


if __name__ == "__main__":
    input_queue = Queue()
    t = ThreadCamera(input_queue)
    t.start()

    limit_time = 10
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            if limit_time < elapsed_time:
                break

            if input_queue.empty():
                continue

            data = input_queue.get()
            roll, pitch, yaw = angles = data[0]
            print(f"\tGETTING ANGLES = R:{roll:7.2f}, P:{pitch:7.2f}, Y:{yaw:7.2f}")
    finally:
        t.lock.acquire()
        t.exit_flag = True
        t.lock.release()
        t.join()

