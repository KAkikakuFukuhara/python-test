""" Canvas: 画像の表示
"""
import tkinter as tk

from pathlib import Path

if __name__ == "__main__":
    test_img_path = Path("shiba.png")
    assert test_img_path.exists()

    root = tk.Tk()

    width = 640
    height = 480
    bg_color = 'white' # background color
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()

    img = tk.PhotoImage(file=test_img_path)
    canvas.create_image(0, 0, image=img, anchor='nw')

    root.mainloop()
