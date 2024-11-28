""" チェックボタンのクリック時の挙動
"""
import tkinter as tk


def callback(*args, **kwargs):
    print(bool_var.get())



if __name__ == "__main__":
    root = tk.Tk()

    bool_var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(root, text="check button", variable=bool_var)
    checkbutton.pack()
    ### ボタンがクリックされた時には値が変わっていない
    checkbutton.bind("<Button-1>", callback)
    ### ボタンをクリックして離した時に値が変わっている
    checkbutton.bind("<ButtonRelease>", callback)

    root.mainloop()
