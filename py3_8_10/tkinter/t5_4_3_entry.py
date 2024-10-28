""" Entry: 入力された文字列を削除する
"""
import tkinter as tk

def callback(*args):
    """ Entryに記述された文字列を出力する。
    ついでに削除する。
    """
    text: str = entry.get()
    print(text)
    ### 削除
    ## どこからどこまで削除するか指定
    ## tk.ENDは行末まで
    entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="print")
    button.pack()

    button.bind("<Button-1>", func=callback)
    root.mainloop()
