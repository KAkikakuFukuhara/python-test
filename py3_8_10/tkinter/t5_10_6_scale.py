""" scale:値の動的変更
"""
import tkinter as tk
import random


def get_new_max_num():
    max_num = random.randint(10, 10000)
    return max_num


def callback(*args):
    max_num = get_new_max_num()
    scale.config(to=max_num)
    scale.set(0)


if __name__ == "__main__":
    root = tk.Tk()

    scale = tk.Scale(root, from_=0, to=100)
    scale.pack()

    button = tk.Button(root, text="Update")
    button.pack()
    button.bind("<Button-1>", callback)

    root.mainloop()