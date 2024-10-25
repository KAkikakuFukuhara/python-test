""" Buttonの配置
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="button-1")
    button.pack()

    root.mainloop()