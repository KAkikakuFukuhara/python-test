""" packによる配置
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button1 = tk.Button(root, text="Button 1")
    button1.pack()
    button2 = tk.Button(root, text="Button 2")
    # button2.pack()
    button3 = tk.Button(root, text="Button 3")
    # button3.pack()
    button4 = tk.Button(root, text="Button 4")
    # button4.pack()

    root.mainloop()
