""" ボタンの配置（ウィジェットの配置）
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### ボタンの配置
    button = tk.Button(root, text="This is Button")
    button.pack()

    root.mainloop()
