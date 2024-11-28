""" チェックボタン
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    checkbutton = tk.Checkbutton(root, text="check button")
    checkbutton.pack()

    root.mainloop()
