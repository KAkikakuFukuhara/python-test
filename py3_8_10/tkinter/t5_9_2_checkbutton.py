""" チェックボタンの値の参照
"""
import tkinter as tk


def callback(*args, **kwargs):
    print(bool_var.get())



if __name__ == "__main__":
    root = tk.Tk()

    bool_var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(root, text="check button", variable=bool_var)
    checkbutton.pack()

    button = tk.Button(root, text="Print")
    button.pack()
    button.bind("<Button-1>", callback)

    root.mainloop()
