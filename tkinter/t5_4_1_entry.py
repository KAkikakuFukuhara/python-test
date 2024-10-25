""" Entry:１行のテキストボックス
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    ### ユーザーが書き込める1行テキストボックスの作成
    ## 文字を書き込める
    entry = tk.Entry(root)
    entry.pack()

    root.mainloop()
