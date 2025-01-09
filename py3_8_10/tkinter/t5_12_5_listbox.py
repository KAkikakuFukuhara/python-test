""" listbox: show last string end
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

    ### horizontal scrollbar
    scrollbar = tk.Scrollbar(root, orient="horizontal")
    scrollbar.grid(row=1, column=0, sticky=tk.W+tk.E)
    scrollbar.config(command=listbox.xview)
    listbox.config(xscrollcommand=scrollbar.set)

    ### insert multiple string
    for i in range(100):
        listbox.insert(i, f"/home/test/test/test/test/test/test/{i}.jpg")

    ### X方向の最後尾を表示する
    listbox.xview_moveto(1.0)

    root.mainloop()
