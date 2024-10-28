""" マルチプロセッシングにおけるpipe通信
"""
import multiprocessing
import time

import numpy as np
import cv2
import matplotlib.pyplot as plt

def func(pipe:multiprocessing.Pipe) -> None:
    """ pipeを通じて画像を受信したらリサイズして返却する
    """
    while True:
        if not pipe.poll():
            continue
    
        image = pipe.recv()
        height, width = image.shape[:2]
        image = cv2.resize(image, (width // 2, height // 2))
        pipe.send(image)

def main():
    """ main
    """

    org = np.random.randint(0, 255, (480, 640, 3)).astype("uint8")
    plt.imshow(org)
    plt.show()

    parent_pipe, child_pipe = multiprocessing.Pipe()

    p = multiprocessing.Process(target=func, args=(child_pipe, ), daemon=True)
    p.start()

    elapsed_times = []
    for i in range(10):
        start_time = time.time()
        parent_pipe.send(org)
        while True:
            if parent_pipe.poll():
                break
            if not p.is_alive():
                print("Process is Deth")
                return 
    
        result = parent_pipe.recv()
        elapsed_time = time.time() - start_time
        print(f"Elapsed_time : {elapsed_time}")
        elapsed_times.append(elapsed_time)

    print(f"Average Elapsed Time : {sum(elapsed_times) / len(elapsed_times)}")
    plt.imshow(result)
    plt.show()

if __name__ == "__main__":
    main()
