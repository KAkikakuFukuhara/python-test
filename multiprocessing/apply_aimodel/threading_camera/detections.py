""" マルチプロセスを用いた物体検出関数
"""
import signal
import sys
from multiprocessing import Queue
from numpy import ndarray

import models

###############################
# begin "def sigterm"
###############################
def sigterm_func(sig_num, frame):
    """ サブプロセス終了時にSIGTERMが呼ばれた際にハンドルされる関数
    """
    print("[Info type=System] Call SIGTERM")
    sys.exit(0)

###############################
# begin "def detect"  
################################
def detect(in_q:Queue, out_q:Queue) -> None:
    """ 物体検出を行う関数
    詳細：
        １．画像が送られてくるまで queue.Queue.get() で待機する。
        ２．画像が送られてくると物体検出を行う。
        ３．検出結果を queue.Queue.put()で送信する
    引数：
        in_q : multiprocessing.Queue
            画像を受診するキュー
        out_q : multiprocessing.Queue
            検出結果を送信するキュー
    """
    signal.signal(signal.SIGTERM, sigterm_func)
    model = models.Model()
    print("[Info type=System] Detection Process is able to start")
    try:
        while True:
            recv_data = in_q.get(block=True, timeout=None)
            if not isinstance(recv_data, ndarray):
                print(f"[Info type=DataError] recv_data is not ndarray, recv_data is {type(recv_data)}")
                continue
            elif len(recv_data.shape) != 3:
                print(f"[Info type=DataError] recv_data's shape is not image shape, recv_data shape is {len(recv_data.shape)}")
                continue
            elif recv_data.shape[2] != 3:
                print(f"[Info type=DataError] recv_data's channel size is not image, recv_data's channel shape id {recv_data.shape[2]}")
                continue
            else:
                image = recv_data

            model.detect(image)
            objs = model.get_detect_objects()
            out_q.put(objs)
    finally:
        print("[Info type=System] Exit Detection Process")
# end "def detect"

##############################
# begin "def test"
##############################
def test():
    from multiprocessing import Process
    import numpy as np
    
    image_queue, result_queue = Queue(), Queue()
    p = Process(target=detect, args=(image_queue, result_queue, ), daemon=True)
    p.start()
    
    image : ndarray = (np.ones((480, 640, 3)) * [255, 0, 0]).astype("uint8")

    try:
        print("Start Push")
        image_queue.put(image)
        print("start Get")
        result = result_queue.get()
        print("finsh get")
        print(result)
        print("Start Push")
        image_queue.put(image)
    finally:
        pass
# end "def test"

if __name__ == "__main__":
    test()


    
