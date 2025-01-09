""" scrollbar
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack()

    root.mainloop()