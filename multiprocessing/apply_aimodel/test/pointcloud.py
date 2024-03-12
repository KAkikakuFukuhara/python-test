""" pyrealsenseを使用したポイントクラウドの生成
"""
import time
from queue import Queue

import numpy as np
import pyrealsense2 as rs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

LIMIT_TIME = 3

pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.gyro)
config.enable_stream(rs.stream.accel)
align_to = rs.stream.color
align = rs.align(align_to)

frame_times = []
system_times = []
first_flag = True


try:
    print("カメラ起動開始")
    profile = pipe.start()
    depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
except Exception as e:
    print(e)
else:
    print("カメラ起動成功")
    for i in range(3):
        print(f"\rカメラ準備中{'.' * (i+1)}", end="")
        time.sleep(0.5)
    try:
        while True:
            frames  = pipe.wait_for_frames()
            frame_time = frames.get_timestamp()
            system_time = time.time()
            if first_flag:
                first_flag = False
                first_time = system_time

            if system_time - first_time > LIMIT_TIME:
                break

            frame_times.append(frame_time)
            system_times.append(system_time)
            #time.sleep(0.1)
    finally:
        print("カメラ停止")
        pipe.stop()

frame_times = np.array(frame_times)
frame_times -= frame_times[0]
system_times = np.array(system_times)
system_times -= system_times[0]
int_f_times = ( frame_times * 1e-3 ).astype(int)
int_s_times = system_times.astype(int)
f_hist = np.histogram(int_f_times, bins=range(0, LIMIT_TIME+1))[0]
s_hist = np.histogram(int_s_times, bins=range(0, LIMIT_TIME+1))[0]

print("frames_histogram")
print(f"\t{f_hist}")
print("system_histogram")
print(f"\t{s_hist}")

frames = align.process(frames)
depth_frame = frames.get_depth_frame()
color_frame = frames.get_color_frame()
depth_intrin = depth_frame.profile.as_video_stream_profile().intrinsics
pc_start_time = time.time()
pointcloud = rs.pointcloud()
point_data = pointcloud.calculate(depth_frame)
v = point_data.get_vertices()
verts = np.asanyarray(v).view("float32").reshape(-1, 3) * 1000
pc_finsh_time = time.time()
print(f"Make PointCloud ElapsedTime:{pc_finsh_time - pc_start_time}")
loop_start_time = time.time()
pc_list = []
for i in range(480):
    for j in range(640):
        depth = depth_frame.get_distance(j, i)
        point = rs.rs2_deproject_pixel_to_point(depth_intrin, [j, i], depth)
        pc_list.append(point)
loop_finsh_time = time.time()
print(f"Loop PointCould ElapsedTime:{loop_finsh_time - loop_start_time}")

color_data = np.asanyarray(color_frame.get_data()).reshape(-1, 3)
args = np.where(np.logical_and(verts[:, -1] < 1000, verts[:, -1] > 0))
points = verts[args[0]]
color_data = color_data[args[0]]

def point_to_3d(points:np.ndarray, color_data:np.ndarray):
    """ ポイントとカラーを与えると三次元上にプロットしてくれる関数
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("width")
    ax.set_ylabel("depth")
    ax.set_zlabel("height")

    x = points[:, 0]
    y = points[:, 1] * -1
    z = points[:, 2]
    ax.scatter(x, z, y, s=1, c=color_data/255)
    
    plt.show()

point_to_3d(points, color_data)
