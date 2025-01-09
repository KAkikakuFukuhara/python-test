""" listbox: sticky expand
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")

    ### add weight
    ## https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    listbox = tk.Listbox(root)
    listbox.grid(row=0, column=0, sticky=tk.NSEW)

    listbox = tk.Listbox(root)
    listbox.grid(row=1, column=1, sticky=tk.NSEW)

    print("Lets resize window!!!!")

    root.mainloop()
