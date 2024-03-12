import random
import time
import tkinter as tk
from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import cv2

from app_module import draw
from app_module import canvas_gui



def make_random_rect(height:int=480, width:int=640) -> Tuple[int]:
    w = random.randint(0, width - int(width / 4))
    e = random.randint(w, width-1)
    n = random.randint(0, height - int(height / 4))
    s = random.randint(n, height-1)
    return n, w, s, e

def resize_image(image:np.ndarray) -> np.ndarray:
    height = image.shape[0]
    width = image.shape[1]
    image = cv2.resize(image, (int(width*0.5), int(height*0.5)))
    return image

def color_generator():
    red = [128, 0, 0]
    green = [0, 128, 0]
    bleu = [0, 0, 128]
    yellow = [128, 128, 0]
    cyan = [0, 128, 128]
    magenta = [128, 0, 128]
    """
    a1 = [0 for i in range(3)]
    a2 = [1*(2**4) for i in range(3)]
    a3 = [2*(2**4) for i in range(3)]
    a4 = [3*(2**4) for i in range(3)]
    a5 = [4*(2**4) for i in range(3)]
    a6 = [5*(2**4) for i in range(3)]
    a7 = [6*(2**4) for i in range(3)]
    a8 = [7*(2**4) for i in range(3)]
    """
    color_list = [red, green, bleu, yellow, cyan, magenta]
    while True:
        for color in color_list:
            yield color

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("+0+0")

        self.canvas = canvas_gui.ImageCanvas(self)
        self.canvas.pack()
        self.button_start = tk.Button(self, text="start", command=self._start)
        self.button_start.pack()
        self.button_exit = tk.Button(self, text="exit", command=self.exit)
        self.button_exit.pack()

        self.after_id = None
        self.color_gen = color_generator()

        self.ppe = ProcessPoolExecutor()
        self.future = None

    def _start(self):
        self.button_start.config(state="disable")
        self.update_frames()

    def exit(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.ppe.shutdown()
        self.destroy()

    def update_frames(self):
        image = np.ones((480, 640, 3)) * next(self.color_gen)
        result = image.copy()
        if self.future is None:
            self.start = time.time()
            self.future = self.ppe.submit(resize_image, image)
        else:
            if self.future.done():
                result = self.future.result()
                elapsed_time = time.time() - self.start
                print(f"elapsed_time:{elapsed_time}")
                self.future = None

        self.canvas.create_color_canvas(result.astype("uint8"))
        self.after_id = self.after(10, self.update_frames)

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()