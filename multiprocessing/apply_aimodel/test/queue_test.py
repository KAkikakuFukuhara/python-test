""" マルチプロセッシングにおけるpipe通信
"""
import multiprocessing
import time

import numpy as np
import cv2
import matplotlib.pyplot as plt

def func(r_queue:multiprocessing.Queue, s_queue:multiprocessing.Queue) -> None:
    """ queueを通じて画像をやり取りする
    """
    while True:
        if r_queue.empty():
            continue
    
        image = r_queue.get()
        height, width = image.shape[:2]
        image = cv2.resize(image, (width // 2, height // 2))
        s_queue.put(image)

def main():
    """ main
    """

    org = np.random.randint(0, 255, (480, 640, 3)).astype("uint8")
    plt.imshow(org)
    plt.show()

    r_queue = multiprocessing.Queue()
    s_queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=func, args=(s_queue, r_queue), daemon=True)
    p.start()

    elapsed_times = []
    for i in range(10):
        start_time = time.time()
        s_queue.put(org)
        while True:
            if not r_queue.empty():
                break
            if not p.is_alive():
                print("Process is Deth")
                return 
    
        result = r_queue.get()
        elapsed_time = time.time() - start_time
        print(f"Elapsed_time : {elapsed_time}")
        elapsed_times.append(elapsed_time)

    print(f"Average Elapsed Time : {sum(elapsed_times) / len(elapsed_times)}")

    plt.imshow(result)
    plt.show()

if __name__ == "__main__":
    main()
