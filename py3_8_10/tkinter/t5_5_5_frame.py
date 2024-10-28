""" Frame:ウィジェットの内包しているモノは以下で参照できる
"""
import tkinter as tk
import pprint

def make_widgets(frame):
    ### rootに配置(grid)
    button1 = tk.Button(frame, text="Button-1")
    button1.grid(row=0, column=0)
    button2 = tk.Button(frame, text="Button-2")
    button2.grid(row=0, column=1)
    button3 = tk.Button(frame, text="Button-3")
    button3.grid(row=1, column=0)
    button4 = tk.Button(frame, text="Button-4")
    button4.grid(row=1, column=1)


if __name__ == "__main__":
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    make_widgets(frame)

    ### childrenに配置してあるウィジェットが辞書型で参照できる
    pprint.pprint(frame.children)

    ### tk.Tkも同じように
    print("--------------------")
    pprint.pprint(root.children)

    root.mainloop()
