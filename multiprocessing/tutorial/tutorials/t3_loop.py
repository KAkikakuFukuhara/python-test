""" 10秒間サブプロセスが動作するプログラム
"""
import multiprocessing as mp
import time

def func():
    try:
        while(True):
            y = time.time()
            print(f"time:{y}")

            time.sleep(1)
    finally:
        print("finish")


if __name__ == "__main__":
    p = mp.Process(target=func, daemon=True)
    p.start()

    time.sleep(10)

