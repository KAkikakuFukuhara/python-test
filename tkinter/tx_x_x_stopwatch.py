""" ストップウォッチ
"""
import tkinter as tk
import time
import datetime

pre_time = None
after_id = None


def update_time():
    global pre_time
    if pre_time is None:
        pre_time = datetime.datetime.now()
    else:
        elapd_time = datetime.datetime.now() - pre_time
        label['text'] = elapd_time
    global after_id
    after_id = root.after(10, update_time)


def callback(event):
    if button['state'] == 'disabled':
        return
    button.config(state='disabled')

    update_time()


def callback2(event):
    if after_id is not None:
        root.after_cancel(after_id)
        button.config(state='normal')


def callback3(event):
    global pre_time
    if pre_time is not None:
        pre_time = None
        label.config(text=f"{datetime.time(0, 0, 0, 0)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("480x360")

    label = tk.Label(root, text=f"{datetime.time(0, 0, 0, 0)}")
    label.pack(expand=1)

    button = tk.Button(root, text="Start")
    button.pack()
    button.bind("<Button-1>", callback)

    button2 = tk.Button(root, text="Stop")
    button2.pack()
    button2.bind("<Button-1>", callback2)

    button3 = tk.Button(root, text="Reset")
    button3.pack()
    button3.bind("<Button-1>", callback3)

    root.mainloop()


