""" 3つのプロセスをそれぞれ起動するプログラム
A:メインプロセス
    Bにデータを要求してBにデータを送信させる
    Cに結果があればCからも結果を受け取る
B:計算を保持し続けるプロセス
    Aから要求があればデータをAに送信する
    Aから要求があればデータをCに送信する
C:データを受け取ると処理を行うプロセス
    Bからデータを受け取ると計算結果をAに送る
"""

import tkinter as tk
import time
import sys
import signal
from multiprocessing import Queue, Process
from typing import List

def termed(sig_num, frame):
    """ daemon　プロセス終了時の処理
    """
    print("EXECUTE SIGTERM")
    sys.exit(0)

def func1(q:List[Queue], p:List[Queue]) -> None:
    """ func1
    """
    signal.signal(signal.SIGTERM, termed)
    recv_queue = q[0]
    send_queue = q[1]
    start = time.time()
    try:
        while True:
            if recv_queue.empty():
                continue

            recv_value = recv_queue.get()
            elapsed_time = time.time() - start
            send_queue.put(round(elapsed_time, 1))
    finally:
        print("func1_finish")

def func2(q:List[Queue]) -> None:
    """ func2
    """
    signal.signal(signal.SIGTERM, termed)
    recv_queue = q[0]
    send_queue = q[1]
    try:
        while True:
            if recv_queue.empty():
                continue

            recv_value = recv_queue.get()
            send_queue.put(i)
            i += 1
            time.sleep(0.25)
    finally:
        print("func2_finish")

class App(tk.Tk):
    """ テスト用のGUI
    """
    def __init__(self):
        super().__init__()
        self.geometry("300x300")

        self.__set_wighet()

        self.queue = [Queue(), Queue()]
        self.p = Process(target=func1, args=(self.queue,), daemon=True)
        self.p.start()
        self.first_flag = True

        self.after_id = None

    def __set_wighet(self):
        """ ウィジェットの配置
        """
        self.label = tk.Label(self, text="0")
        self.label.pack(fill="x")
        self.label2 = tk.Label(self, text="0")
        self.label2.pack(fill="x")

        buttons = tk.Frame(self)
        buttons.pack()
        self.start_button = tk.Button(buttons, text="start", command=self.start)
        self.start_button.pack(side="left")
        exit_button = tk.Button(buttons, text="exit", command=self.exit)
        exit_button.pack(side="left")

    def start(self):
        """ GUI更新開始メソッド
        """
        self.start_button.config(state="disable")
        self.update()

    def exit(self):
        """ GUI終了メソッド
        """
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        self.destroy()

    def update(self):
        """ GUIのアップデート
        """
        if self.first_flag:
            self.queue[0].put(1)
            self.first_flag = False

        if not self.queue[1].empty():
            result = self.queue[1].get()
            self.label.config(text=str(result))
            self.queue[0].put(1)

        self.after_id = self.after(10, self.update)

def main() -> None:
    """ main
    """
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()