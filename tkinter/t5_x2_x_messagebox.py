""" messagebox
"""
from typing import Optional
import tkinter as tk
from tkinter import messagebox

def showInfo(event: tk.Event):
    res: str = messagebox.showinfo("Info", "text")
    print(res)
    ## ok


def showWarn(event: tk.Event):
    res: str = messagebox.showwarning("Warning", "text")
    print(res)
    ## ok


def showError(event: tk.Event):
    res: str = messagebox.showerror("Error", "text")
    print(res)
    ## ok


def askQuestion(event: tk.Event):
    res: str = messagebox.askquestion("Question", "text")
    print(res)
    ## yes no


def askOkCancel(event: tk.Event):
    res: bool = messagebox.askokcancel("OkCancel", "text")
    print(res)


def askTryCancel(event: tk.Event):
    res: bool = messagebox.askretrycancel("RetryCancel", "text")
    print(res)


def askYesNo(event: tk.Event):
    res: bool = messagebox.askyesno("YesNo", "text")
    print(res)


def askYesNoCancel(event: tk.Event):
    res: Optional[bool] = messagebox.askyesnocancel("YesNoCancel", "text")
    print(res)


if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="showInfo")
    button.pack()
    ## Press だとボタンを押した描画が戻らない
    button.bind("<ButtonPress-1>", func=showInfo)
    button = tk.Button(root, text="showWarn")
    button.pack()
    ## Releaseだとボタンを押した描画が戻る時にbindが実行されるから戻る
    button.bind("<ButtonRelease-1>", func=showWarn)
    button = tk.Button(root, text="showError")
    button.pack()
    button.bind("<ButtonRelease-1>", func=showError)
    button = tk.Button(root, text="askQuestion")
    button.pack()
    button.bind("<ButtonRelease-1>", func=askQuestion)
    button = tk.Button(root, text="askOkCancel")
    button.pack()
    button.bind("<ButtonRelease-1>", func=askOkCancel)
    button = tk.Button(root, text="askTryCancel")
    button.pack()
    button.bind("<ButtonRelease-1>", func=askTryCancel)
    button = tk.Button(root, text="askYesNo")
    button.pack()
    button.bind("<ButtonRelease-1>", func=askYesNo)
    button = tk.Button(root, text="askYesNoCancel")
    button.pack()
    button.bind("<ButtonRelease-1>", func=askYesNoCancel)

    root.mainloop()

