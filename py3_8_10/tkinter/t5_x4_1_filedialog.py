""" ファイル指定ウィンドウの作り方
"""
import tkinter as tk
from tkinter import filedialog

def get_file_path(dir_path:str, file_suffix="py") -> str:
    ### 検索したいファイルの種類を決める
    file_types = [
        ### (表示名, "ファイルの種類")
        (f"ファイルタイプ", f"*.{file_suffix}"),
        ("すべてのファイル", "*")
    ]
    file_path = filedialog.askopenfilename(
        filetypes=file_types,
        initialdir=dir_path, #検索対象ディレクトリ
    )

    ### cansel選択時はtupleが返ってくるみたい
    if isinstance(file_path, tuple):
        raise FileNotFoundError("select cancel")
    return file_path


if __name__ == "__main__":
    file_path = get_file_path("./")
    print(file_path)
