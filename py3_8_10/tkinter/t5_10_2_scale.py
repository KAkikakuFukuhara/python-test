""" scale:向き
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    ### 水平方向スライダー
    scale = tk.Scale(root, orient="horizontal")
    scale.pack()
    ### 垂直方向スライダー
    scale2 = tk.Scale(root, orient="vertical")
    scale2.pack()

    root.mainloop()