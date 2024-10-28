""" Labelの配置:ボタンとの組み合わせ
"""
import tkinter as tk


def callback(*args):
    """ ボタンをクリックするたびにLabelの文字が切り替わる
    """
    text = label["text"]
    if text == "Label":
        label["text"] = "Changed!!!"
    else:
        label["text"] = "Label"


if __name__ == "__main__":
    root = tk.Tk()

    label = tk.Label(root, text="Label")
    label.pack()

    button = tk.Button(root, text="Button")
    button.pack()

    button.bind("<Button-1>", callback)

    root.mainloop()