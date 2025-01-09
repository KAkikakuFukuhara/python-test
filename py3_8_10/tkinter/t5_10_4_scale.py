""" scale:値の参照(scale.bind)
"""
import tkinter as tk


def callback(*args, **kwargs):
    print(scale_var.get())


if __name__ == "__main__":
    root = tk.Tk()

    scale_var = tk.IntVar()
    scale = tk.Scale(root, variable=scale_var)
    scale.pack()
    ### クリック時実行
    scale.bind("<Button-1>", callback)
    ### 離した時実行
    scale.bind("<ButtonRelease>", callback)

    root.mainloop()