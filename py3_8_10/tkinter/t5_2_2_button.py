""" Buttonのクリックに連動した処理の実行
"""
import tkinter as tk

def callback(*args):
    print("!!! Button Pushed !!!")

if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="button-1")
    button.pack()

    button.bind("<Button>", func=callback)

    root.mainloop()