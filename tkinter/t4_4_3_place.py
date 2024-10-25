""" placeによる配置（複数
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.place(x=0, y=0)
    button2 = tk.Button(root, text="Button 2")
    button2.place(x=20, y=20)

    root.mainloop()
