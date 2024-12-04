""" listbox
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    listbox = tk.Listbox(root)
    listbox.pack()

    root.mainloop()
