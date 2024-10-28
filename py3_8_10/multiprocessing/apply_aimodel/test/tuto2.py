"""
    マルチプロセッシング基礎2
    継承を使用して行う方法
"""

import multiprocessing
import os, time

TEST_COUNT = 1000000

def calc(count_num):
    i = 0
    for n in range(count_num):
        i += n
    print(f"[end] ret={i:d} (process ID={os.getpid():d})")

class myProcess(multiprocessing.Process):
    def __init__(self, num=10000):
        """ 初期化　計算回数の設定
        """
        self._count_num = num
        super().__init__()

    def run(self):
        """プロセス実行
        """
        tm = time.time()
        calc(self._count_num)
        print(f"[finish] time:{time.time()-tm:f}(sec) (process ID={os.getpid():d})")

def main():
    proc1 = myProcess(TEST_COUNT)
    proc2 = myProcess(TEST_COUNT)

    # 時間計測開始
    tm = time.time()

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    # 終了　時間表示
    print(f"[finish] {time.time()-tm:f}(sec)")

if __name__ == "__main__":
    main()
