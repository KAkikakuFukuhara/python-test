""" listbox: doubleclickEvent
"""
from typing import Tuple
import tkinter as tk


def double_click(event: tk.Event):
    cur_pos: Tuple[int] = listbox.curselection()
    x = listbox.get(cur_pos[0], cur_pos[0])
    print(x)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    listbox = tk.Listbox(root)
    listbox.grid(row=0, column=0)
    listbox.bind("<Double-Button-1>", double_click)

    ### insert multiple string
    for i in range(100):
        listbox.insert(i, str(i))

    root.mainloop()
