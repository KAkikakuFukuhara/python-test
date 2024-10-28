import tkinter as tk
from typing import List, Tuple
import cv2
from PIL import Image, ImageTk
import numpy as np


class CanvasBase(tk.Canvas):
    def __init__(self, master=None, width=640, height=480):
        super().__init__(master, width=width, height=height)
        self.create_rectangle(0, 0, 640, 480, fill='black')
        self.tkimage = None

    def set_tkimage_attr(self, image: np.ndarray) -> None:
        self.image = image
        self.tkimage = ImageTk.PhotoImage(Image.fromarray(image))

    def delete_(self) -> None:
        self.delete("all")

    def get_image(self) -> np.ndarray:
        return self.image.copy()

class ImageCanvas(CanvasBase):
    def __init__(self, master=None, width=640, height=480):
        super().__init__(master, width=width, height=height)
        self.depth_value = 0.1

    def create_color_canvas(self, image: np.ndarray) -> np.ndarray:
        self.set_tkimage_attr(image)
        self.create_image(0, 0, image=self.tkimage, anchor='nw')
    
    def cvt_depth2color(self, image: np.ndarray) -> np.ndarray:
        scaleAbs_image = cv2.convertScaleAbs(image, alpha=self.depth_value)
        return cv2.applyColorMap(scaleAbs_image, cv2.COLORMAP_JET)

    def create_depth_canvas(self, image: np.ndarray) -> None:
        image = self.cvt_depth2color(image)
        self.set_tkimage_attr(image)
        self.create_image(0, 0, image=self.tkimage, anchor='nw')

    def create_compose_canvas(self, color_image: np.ndarray, depth_image: np.ndarray) -> None:
        depth_mask = depth_image > 0
        depth_mask = np.stack([depth_mask, depth_mask, depth_mask], -1)
        compose_image = color_image * depth_mask
        self.create_color_canvas(compose_image)

