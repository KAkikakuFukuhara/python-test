""" Frame:ウィジェットの内包を使わないとt5_3_3のようにできない(このプログラムは失敗します)
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### rootに配置(grid)
    button1 = tk.Button(root, text="Button-1")
    button1.grid(row=0, column=0)
    button2 = tk.Button(root, text="Button-2")
    button2.grid(row=0, column=1)
    button3 = tk.Button(root, text="Button-3")
    button3.grid(row=1, column=0)
    button4 = tk.Button(root, text="Button-4")
    button4.grid(row=1, column=1)

    ### rootに配置(pack)
    button5 = tk.Button(root, text="Button-5")
    button5.pack()

    ### packとgridは同じ階層に混同して配置できない。
    root.mainloop()
