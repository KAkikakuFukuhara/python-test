""" sub menu
"""
import tkinter as tk


if __name__ == "__main__":
    root_view = tk.Tk()
    root_view.geometry("300x300")

    menubar = tk.Menu()
    # menu.pack()
    root_view.config(menu=menubar)
    menubar.add_command(label="Menu1", command=lambda *x: print(x))

    menu2 = tk.Menu()
    menu2.add_command(label="SubMenu1", command=lambda *x:print("Sub1"))
    menu2.add_command(label="SubMenu2", command=lambda *x:print("Sub2"))
    menubar.add_cascade(label="Menu2", menu=menu2)

    root_view.mainloop()


