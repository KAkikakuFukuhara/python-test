""" Buttonが連打されることを防ぐ方法
"""
import tkinter as tk

def prevent_double_click(func):
    def wrapper(*args, **kwargs):
        if button['state'] == 'disabled':
            return
        button.config(state="disabled")
        try:
            func(*args, **kwargs)
        except Exception as e:
            pass
        finally:
            ms = 100 # mill second
            root.after(ms, lambda: button.config(state='normal'))
    return wrapper


@prevent_double_click
def callback(*args):
    """連打対策
    """
    def prod(x, y):
        return x * y
    for i in range(int(1e7)):
        prod(i, i+1)

    print(args)


def disable_button2(func):
    def wrapper(*args, **kwargs):
        print("disable")
        if button2['state'] == 'disabled':
            return
        button2.config(state="disabled")
        ### afterを利用しないとボタンがdisableにならない
        ms = 10
        root.after(ms, func, *args)
    return wrapper


def enable_button2(func):
    def wrapper(*args, **kwargs):
        print("enable")
        func(*args, **kwargs)
        ms = 10
        root.after(ms, lambda:button2.config(state="normal"))
    return wrapper


@disable_button2
@enable_button2
def callback2(*args):
    """連打対策
    """
    def prod(x, y):
        return x * y
    for i in range(int(1e7)):
        prod(i, i+1)

    print(args)

if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="button1")
    button.pack()
    button.bind("<Button-1>", func=callback)

    button2 = tk.Button(root, text="button2")
    button2.pack()
    button2.bind("<Button-1>", func=callback2)

    root.mainloop()
