""" Entry: Buttonと組み合わせて
"""
import tkinter as tk

def callback(*args):
    """ Entryに記述された文字列を出力する
    """
    text: str = entry.get()
    print(text)


if __name__ == "__main__":
    root = tk.Tk()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="print")
    button.pack()

    button.bind("<Button-1>", func=callback)
    root.mainloop()
