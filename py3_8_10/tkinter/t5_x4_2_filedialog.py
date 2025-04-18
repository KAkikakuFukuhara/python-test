""" ファイル指定ウィンドウの作り方（ボタン起動）
"""
import tkinter as tk
from tkinter import filedialog

def get_file_path(dir_path:str, file_suffix="py") -> str:
    file_types = [("", f"*.{file_suffix}")]
    file_path = filedialog.askopenfilename(filetypes=file_types, initialdir=dir_path)
    if type(file_path) != str:
        raise FileNotFoundError
    return file_path


def print_file_path(dir_path:str, file_suffix="py"):
    file_path = get_file_path(dir_path, file_suffix)
    print(file_path)


def on_click(event: tk.Event):
    # ボタン押したままになる対策の解決
    # https://kankisenkowasuo.hatenablog.com/entry/2025/03/12/013448
    root.after(1, print_file_path, ("./"))


if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="Open")
    button.pack()
    button.bind("<Button-1>", on_click)

    root.mainloop()