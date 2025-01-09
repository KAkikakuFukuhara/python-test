""" scale:値の参照
"""
import tkinter as tk


def callback(*args, **kwargs):
    print(scale_var.get())


if __name__ == "__main__":
    root = tk.Tk()

    scale_var = tk.IntVar()
    scale = tk.Scale(root, variable=scale_var)
    scale.pack()

    button = tk.Button(root, text="Print")
    button.pack()
    button.bind("<Button-1>", callback)

    root.mainloop()