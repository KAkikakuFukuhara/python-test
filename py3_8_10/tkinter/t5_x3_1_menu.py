""" menu widget
"""
import tkinter as tk


if __name__ == "__main__":
    root_view = tk.Tk()
    root_view.geometry("300x300")

    menubar = tk.Menu()
    # menu.pack()
    root_view.config(menu=menubar)
    menubar.add_command(label="Menu1", command=lambda *x: print(x))

    root_view.mainloop()


