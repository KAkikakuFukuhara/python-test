""" packによる配置（右詰め
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.pack(side=tk.RIGHT)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(side=tk.RIGHT)

    root.mainloop()
