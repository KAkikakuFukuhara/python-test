""" Frame:ウィジェットの内包効果
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### rootに配置
    frame = tk.Frame(root)
    frame.pack()

    ### frameに４つのボタンを内包させてgridで配置
    button1 = tk.Button(frame, text="Button-1")
    button1.grid(row=0, column=0)
    button2 = tk.Button(frame, text="Button-2")
    button2.grid(row=0, column=1)
    button3 = tk.Button(frame, text="Button-3")
    button3.grid(row=1, column=0)
    button4 = tk.Button(frame, text="Button-4")
    button4.grid(row=1, column=1)

    ### rootに配置
    button5 = tk.Button(root, text="Button-5")
    button5.pack()

    root.mainloop()
