""" scale:応用：別のラベルの表示
"""
import tkinter as tk
import random


def update_label_as_time(*args):
    value = scale_var.get()
    ### hh:mm:ss変換
    hour = value // 3600
    minute = value % 3600 // 60
    second = value % 3600 % 60
    text = f"{hour:02}:{minute:02}:{second:02}/01:00:00"
    label1.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()
    ### hh:mm:ss表示
    label1 = tk.Label(frame, text=f"00:00:00/01:00:00")
    label1.grid(row=0, column=0)
    ### showvalue=Falseにして通常の表示は隠す
    scale_var = tk.IntVar()
    scale = tk.Scale(frame, orient="horizontal", showvalue=False, to=3600, variable=scale_var, length=1000)
    scale.grid(row=1, column=0)
    ### drug-event
    scale.bind("<B1-Motion>", update_label_as_time)

    root.mainloop()