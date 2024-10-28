""" gridによる配置（順番を入れ替える
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.grid(row=1, column=1)
    button2 = tk.Button(root, text="Button 2")
    button2.grid(row=0, column=0)

    root.mainloop()
