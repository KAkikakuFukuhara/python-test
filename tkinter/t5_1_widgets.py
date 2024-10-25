""" いろんなウィジェット
"""
import tkinter as tk

if __name__ == "__main__":
    ### 参考
    ### https://taida-eng.com/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%82%99%E5%BF%98%E9%8C%B2/tkinter-ttk%E3%82%A6%E3%82%A3%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E4%B8%80%E8%A6%A7/#toc4
    root = tk.Tk()

    widgets = [
        tk.Button(root),
        tk.Text(root),
        tk.Label(root),
        tk.Frame(root),
        tk.Entry(root),
        tk.Spinbox(root),
        # tk.Toplevel(root),
        tk.Listbox(root),
        tk.Checkbutton(root),
        tk.Radiobutton(root),
        tk.Scale(root),
        tk.Message(root),
        tk.LabelFrame(root),
        tk.Canvas(root),
        # tk.Menu(root),
        tk.Menubutton(root),
        tk.PanedWindow(root),
    ]
    """
    from tkinter import ttk
    ttk.Combobox(root)
    ttk.Treeview(root)
    ttk.Progressbar(root)
    ttk.Notebook(root)
    """

    for wi in range(len(widgets)):
        widgets[wi].grid(row=0, column=wi)

    root.mainloop()
