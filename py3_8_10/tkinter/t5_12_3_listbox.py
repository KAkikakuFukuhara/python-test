""" listbox: scrollbar
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    listbox = tk.Listbox(root)
    listbox.grid(row=0, column=0)

    ### scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)

    ### insert multiple string
    for i in range(100):
        listbox.insert(i, str(i))

    root.mainloop()
