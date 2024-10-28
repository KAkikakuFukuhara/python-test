""" デーモンスレッドの挙動実験

詳細：
    デーモンスレッドを使用したスレッドが
    メインスレッドの終了時にSIGTERMを吐き出すかを調査
"""

import signal
import sys
import time
from queue import Queue
from threading import Thread



def sigtermd(sig_num, frame) -> None:
    """ デーモンスレッドの終了処理
    """
    print("CALL SIGTERM")
    sys.exit(0)

def func(q:Queue) -> None:
    """ sub thread
    """
    i = 1
    try:
        while True:
            i += 1
            time.sleep(0.2)
    finally:
        print(f"終了：スコア = {i}")
    
def main():
    """ main thread
    """
    signal.signal(signal.SIGTERM, sigtermd)

    q = Queue()

    t = Thread(target=func, args=(q, ), daemon=True)
    t.start()
    for i in range(6):
        print(f"待機{'.' * (i+1)}")
        time.sleep(0.5)

if __name__ == "__main__":
    main()