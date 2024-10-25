""" タブを動的に切り替える方法
"""
from __future__ import annotations
import tkinter as tk

from tkinter import ttk


def chage_tab_focus(event: tk.Event):
    ### 現在のタブ番号の取得
    tabs: list[str] = notebook.tabs()
    current_tab_name: str = notebook.select()
    current_tab_id: int = tabs.index(current_tab_name)

    ### 新しいタブへの切り替え
    new_tab_id: int = current_tab_id + 1 if current_tab_id < len(tabs)-1 else 0
    notebook.select(new_tab_id)


if __name__ == "__main__":
    root = tk.Tk()

    notebook = ttk.Notebook(root)
    notebook.pack()

    ### tab 1
    frame = tk.Frame(notebook)
    notebook.add(frame, text="tab1")
    canvas1 = tk.Canvas(frame, width=480, height=480, bg="white")
    canvas1.pack()

    ### tab 2
    frame2 = tk.Frame(notebook)
    notebook.add(frame2, text="tab2")
    canvas2 = tk.Canvas(frame2, width=480, height=480, bg="black")
    canvas2.pack()

    ### tab 3
    frame3 = tk.Frame(notebook)
    notebook.add(frame3, text="tab3")
    canvas3 = tk.Canvas(frame3, width=480, height=480, bg="gray")
    canvas3.pack()

    button = tk.Button(root, text="change tab")
    button.pack()
    button.bind("<Button-1>", chage_tab_focus)

    root.mainloop()

