""" pipeを使ったプロセス間通信
"""
import sys
import time
import signal
import multiprocessing as mp
from multiprocessing.connection import PipeConnection


def signal_handler(signum, frame):
    sys.exit(1)


def func(pipe: PipeConnection):
    signal.signal(signal.SIGTERM, signal_handler)
    try:
        while(True):
            obj = pipe.recv()
            print(obj)
    finally:
        print("finish")


if __name__ == "__main__":
    pipe1: PipeConnection; pipe2: PipeConnection
    pipe1, pipe2 = mp.Pipe()
    p = mp.Process(target=func, args=(pipe2, ), daemon=True)
    p.start()

    for i in range(1, 6):
        pipe1.send(i)
        time.sleep(1)

