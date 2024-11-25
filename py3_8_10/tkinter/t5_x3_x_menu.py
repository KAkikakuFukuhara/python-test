""" open file dialog by menu
"""
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as tkfd


def open_dir(*args):
    """ dirのみ選択可能
    """
    file_dir = Path(__file__).absolute().parent
    selected = tkfd.askdirectory(initialdir=str(file_dir.parent))
    print(selected)


def open_file(*args):
    """ ファイルのみ選択可能
    """
    file_dir = Path(__file__).absolute().parent
    selected = tkfd.askopenfilename(initialdir=str(file_dir.parent))
    print(selected)


def open_md(*args):
    """ .mdファイルのみ選択可能(*.pyファイルは見えなくなる)
    """
    file_dir = Path(__file__).absolute().parent
    file_types = [("マークダウン", "*.md", ),]
    selected = tkfd.askopenfilename(filetypes=file_types, initialdir=str(file_dir.parent))
    print(selected)


if __name__ == "__main__":
    root_view = tk.Tk()
    root_view.geometry("300x300")

    menubar = tk.Menu()
    # menu.pack()
    root_view.config(menu=menubar)
    menubar.add_command(label="OpenDir", command=open_dir)
    menubar.add_command(label="OpenFile", command=open_file)
    menubar.add_command(label="OpenMd", command=open_md)

    root_view.mainloop()


