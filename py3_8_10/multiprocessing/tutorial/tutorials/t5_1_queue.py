""" queueを使ったプロセス間通信
"""
import sys
import time
import signal
import multiprocessing as mp


def signal_handler(signum, frame):
    sys.exit(1)


def func(q:mp.Queue):
    signal.signal(signal.SIGTERM, signal_handler)
    try:
        while(True):
            obj = q.get()
            print(q)
    finally:
        print("finish")


if __name__ == "__main__":
    queue = mp.Queue(maxsize=1)
    p = mp.Process(target=func, args=(queue, ), daemon=True)
    p.start()


    for i in range(1, 6):
        queue.put(i)
        time.sleep(1)
