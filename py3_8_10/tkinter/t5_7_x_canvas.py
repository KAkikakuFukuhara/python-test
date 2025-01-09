""" Widgetをキャンバスに埋め込み。
今回は黒背景のキャンバスウィジェットを埋め込み
"""

import tkinter as tk
from typing import Literal

canvas_width = 600
canvas_height = 600
widgets = []


def AddCanvasIntoCanvas(event: tk.Event):
    width = 99
    height = 99
    num_column_widget = canvas_width // width # limitation
    col_num = len(widgets) % num_column_widget
    row_num = len(widgets) // num_column_widget
    px = (1+width) * col_num
    py = (1+height) * row_num
    inner_canvas = tk.Canvas(root_view.canvas, width=width, height=height, bg="black")
    root_view.canvas.create_window(px, py, window=inner_canvas, anchor='nw')
    widgets.append(inner_canvas)
    root_view.button.update()


class RootView(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas = tk.Canvas(self, width=600, height=600, bg="white")
        self.canvas.pack()

        self.button = tk.Button(self, text="Add")
        self.button.pack()
        self.button.bind("<Button-1>", AddCanvasIntoCanvas)


if __name__ == "__main__":
    root_view = RootView()
    root_view.mainloop()

