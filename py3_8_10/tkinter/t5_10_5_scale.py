""" scale:値の参照(小数)
"""
import tkinter as tk


def callback(*args, **kwargs):
    print(scale_var.get())


if __name__ == "__main__":
    root = tk.Tk()

    scale_var = tk.DoubleVar()
    ### from_, to で範囲指定, resolutionでステップ数指定
    scale = tk.Scale(root, variable=scale_var, from_=0, to=1, resolution=0.1)
    scale.pack()
    ### 離した時実行
    scale.bind("<ButtonRelease>", callback)

    root.mainloop()