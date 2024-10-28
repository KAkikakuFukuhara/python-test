import tkinter as tk

from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()

    x = ttk.Notebook(root)
    x.pack()

    frame = tk.Frame(x)
    x.add(frame, text="tab1")
    frame2 = tk.Frame(x)
    x.add(frame2, text="tab2")

    canvas1 = tk.Canvas(frame, width=480, height=480, bg="white")
    canvas1.pack()
    canvas2 = tk.Canvas(frame2, width=480, height=480, bg="black")
    canvas2.pack()


    root.mainloop()

