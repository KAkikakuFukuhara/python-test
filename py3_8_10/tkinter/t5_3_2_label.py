""" Labelの配置:文字の挿入
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    label = tk.Label(root, text="Label")
    label.pack()

    label['text'] = "Changed"

    root.mainloop()