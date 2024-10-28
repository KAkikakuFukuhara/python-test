""" Queueにdepth_frameを挿入できるかテスト
"""
import time
from queue import Queue

import numpy as np
import pyrealsense2 as rs

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

print("Queueに入るかのテスト")
q = Queue()
q.put(frames)
f = q.get()
print(type(f))

#depth_frame = frames.get_depth_frame()
#depth_intrin = depth_frame.profile.as_video_stream_profile().intrinsics
