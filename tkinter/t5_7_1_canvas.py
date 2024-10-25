""" Canvas:
"""
import tkinter as tk

from pathlib import Path

if __name__ == "__main__":
    root = tk.Tk()

    width = 640
    height = 480
    bg_color = 'white' # background color
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()

    ### ボックスの作成
    ## create_rectangle(x1, y1, x2, y2)
    ## 座標1:(x1, y1), 座標2:(x2, y2)の座標を対角に持つボックス
    canvas.create_rectangle(10, 10, 110, 110)
    ## outline=color で線の色を決定
    canvas.create_rectangle(30, 30, 90, 90, outline="red")
    ## fill=color で塗りつぶし色を決定. 色コードも使える
    canvas.create_rectangle(50, 50, 70, 70, fill="#ff00ff")

    root.mainloop()
