""" プロセスをkillしてもfinally節が実行されるプログラム
"""
import sys
import signal
import multiprocessing as mp
import time

import tutorials.t3_loop as t3_loop

def signal_handler(signum, frame):
    sys.exit(1)


def func():
    signal.signal(signal.SIGTERM, signal_handler)
    t3_loop.func()


if __name__ == "__main__":
    p = mp.Process(target=func, name="t4_func", daemon=True)
    p.start()

    time.sleep(100)

