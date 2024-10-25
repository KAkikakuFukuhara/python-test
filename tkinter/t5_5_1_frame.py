""" Frame:ウィジェットを内包することができる
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    ### rootの変わりにコンストラクタ(__init__)に渡せる
    ## tk.Button(root) -> tk.Button(frame)
    button1 = tk.Button(frame, text="Button-1")
    button1.pack()
    button2 = tk.Button(frame, text="Button-2")
    button2.pack()
    button3 = tk.Button(frame, text="Button-3")
    button3.pack()
    button4 = tk.Button(frame, text="Button-4")
    button4.pack()

    root.mainloop()
