""" placeによる配置(位置を指定しない)
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.place()

    root.mainloop()
