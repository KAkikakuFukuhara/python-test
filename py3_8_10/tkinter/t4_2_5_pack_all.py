""" packによる配置（いろんな方向
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.pack(side=tk.TOP)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(side=tk.LEFT)
    button3 = tk.Button(root, text="Button 3")
    button3.pack(side=tk.BOTTOM)
    button4 = tk.Button(root, text="Button 4")
    button4.pack(side=tk.RIGHT)

    root.mainloop()
