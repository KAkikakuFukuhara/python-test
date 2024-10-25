""" Canvas:描画オブジェクトの動的作成
"""
import tkinter as tk


def callback(event: tk.Event):
    """ マウスが押された座標にボックスを作成する
    """
    cx = event.x
    cy = event.y

    x1 = cx - 5
    y1 = cy - 5
    x2 = cx + 5
    y2 = cy + 5

    canvas.create_rectangle(x1, y1, x2, y2, fill="red")


if __name__ == "__main__":
    root = tk.Tk()

    width = 640
    height = 480
    bg_color = 'white' # background color
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()

    ### canvasにマウスクリックを紐付ける
    canvas.bind("<Button-1>", callback)


    root.mainloop()
