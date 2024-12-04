""" scrollbar: リストボックスの編集
"""
from typing import Tuple
import tkinter as tk


def add(event: tk.Event):
    """ 最後尾に追加
    """
    num_items = listbox.size()
    listbox.insert(num_items+1, "ADD")


def read(event: tk.Event):
    """ 現在選択している値を表示
    """
    curr_pos: Tuple[int] = listbox.curselection()
    print(curr_pos)
    if len(curr_pos) != 0:
        curr_value: Tuple[int] = listbox.get(curr_pos[0], curr_pos[0])
        print(curr_value[0])


def update(event: tk.Event):
    """ 選択箇所に'Update'を挿入
    """
    new_text = "Update"
    curr_pos: Tuple[int] = listbox.curselection()
    print(curr_pos)
    if len(curr_pos) != 0:
        listbox.delete(curr_pos[0])
        listbox.insert(curr_pos[0], new_text)


def delete(event: tk.Event):
    """ 選択箇所を削除
    """
    curr_pos: Tuple[int] = listbox.curselection()
    print(curr_pos)
    if len(curr_pos) != 0:
        listbox.delete(curr_pos[0])


def delete_all(event: tk.Event):
    listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")


    listbox = tk.Listbox(root)
    listbox.pack()

    ### 値の挿入：挿入箇所と挿入データを用いる
    values = ['tkinter', 'listbox', 'test']
    for vi, v in enumerate(values):
        listbox.insert(vi, v)

    ### CRUD: Create Read Update Delete
    add_button = tk.Button(root, text="ADD")
    add_button.pack()
    add_button.bind("<Button-1>", add)
    read_button = tk.Button(root, text="READ")
    read_button.pack()
    read_button.bind("<Button-1>", read)
    update_button = tk.Button(root, text="UP")
    update_button.pack()
    update_button.bind("<Button-1>", update)
    delete_button = tk.Button(root, text="DEL")
    delete_button.pack()
    delete_button.bind("<Button-1>", delete)
    delete_all_button = tk.Button(root, text="DELALL")
    delete_all_button.pack()
    delete_all_button.bind("<Button-1>", delete_all)

    root.mainloop()
