""" スレッドの挙動実験

詳細：
    スレッドの正常終了ができるサンプルプログラム
"""

import signal
import sys
import time
from queue import Queue
from threading import Thread, Lock

EXECUTE_FLAG = True

def sigtermd(sig_num, frame) -> None:
    """ デーモンスレッドの終了処理
    """
    print("CALL SIGTERM")
    sys.exit(0)

def func(q:Queue, l:Lock) -> None:
    """ sub thread
    """
    i = 1
    try:
        while True:
            lock_start_time = time.time()
            
            # check state MainThread
            l.acquire(0)
            if not EXECUTE_FLAG:
                l.release()
                break
            else:
                l.release()

            lock_finsh_time = time.time()
            print(f"Lock Elapsed_Time:{lock_finsh_time - lock_start_time:.8f}")
            
            i += 1
            time.sleep(0.2)
    finally:
        print("EXIT SubThread")
        print(f"\t Score = {i}")
    
def main():
    """ main thread
    """
    signal.signal(signal.SIGTERM, sigtermd)
    global EXECUTE_FLAG

    q = Queue()
    l = Lock()

    t = Thread(target=func, args=(q, l))

    try:
        t.start()
        for i in range(6):
            print(f"待機{'.' * (i+1)}")
            time.sleep(0.5)
    finally:
        print("Exit MainThread")
        l.acquire()
        EXECUTE_FLAG = False
        l.release()
        t.join()

        
if __name__ == "__main__":
    main()