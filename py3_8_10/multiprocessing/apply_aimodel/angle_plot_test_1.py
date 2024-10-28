""" カメラから映像を取得して物体検出を行うプログラム
    物体検出はマルチプロセス上で実施する
"""
import multiprocessing
import tkinter as tk
from typing import List, Tuple
import random
import time
import signal

import numpy as np
import cv2
import tensorflow as tf

import canvas_gui
import draw
import cameras
import models

# variables
camera = cameras.CameraWithIMU()

class Object:
    def __init__(self, name, rect_wn, rect_es, prob, cw, ch):
        self.name = name
        self.rect_wn = rect_wn
        self.rect_es = rect_es
        self.score = prob
        self.cw = cw
        self.ch = ch
        self.nearest_flag = False
    
    def is_nearest(self) -> bool:
        return self.nearest_flag

def resize_image(r_queue:multiprocessing.Queue, s_queue:multiprocessing.Queue) -> None:
    """ 画像をリサイズする
    """
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            print("elapsed_time over 3 minite")
            break

        if r_queue.empty():
            continue

        image = r_queue.get()
        height = image.shape[0]
        width = image.shape[1]
        result_image = cv2.resize(image, (int(width*0.5), int(height*0.5)))
        s_queue.put(result_image)
    print("process_exit")

def detection_object_with_pipe(pipe:multiprocessing.Pipe) -> None:
    """ 物体検出を行う処理（今回は単純に物体の確率を出力するだけ）
    """
    start_time = time.time()
    #model = make_model()
    model = models.Model()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            break

        if not pipe.poll():
            continue

        image = pipe.recv()
        model.detect(image)
        objs = model.get_detect_objects()
        pipe.send(objs)


def detection_object(r_queue:multiprocessing.Queue, s_queue:multiprocessing.Queue) -> None:
    """ 物体検出を行う処理（今回は単純に物体の確率を出力するだけ）
    """
    start_time = time.time()
    #model = make_model()
    model = models.Model()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            break

        if r_queue.empty():
            continue

        image = r_queue.get()
        model.detect(image)
        objs = model.get_detect_objects()
        s_queue.put(objs)


class LabelWithHorm(tk.Frame):
    """ ラベルとフォームのセットのGUIオブジェクト
    """
    def __init__(self, master=None, label_text="None", form_text="None"):
        super().__init__(master)
        self.label = tk.Label(self, text=label_text, anchor="s")
        self.label.pack(fill="x")
        self.form = tk.Entry(self, text=form_text, anchor="s")
        self.form.pack(fill="x")

class AngleFrame(tk.Frame):
    """ カメラ角度のGUI
    """
    def __init__(self, master=None):
        super().__init__(master)
        none_text = " " * 2 + "None,"
        r_label = tk.Label(self, text="R:")
        p_label = tk.Label(self, text="P:")
        y_label = tk.Label(self, text="Y:")
        self.r_value_label = tk.Label(self, text=none_text)
        self.p_value_label = tk.Label(self, text=none_text)
        self.y_value_label = tk.Label(self, text=none_text)
        r_label.pack(side="left")
        self.r_value_label.pack(side="left")
        p_label.pack(side="left")
        self.p_value_label.pack(side="left")
        y_label.pack(side="left")
        self.y_value_label.pack(side="left")

    def set_angle(self, r:float, p:float, y:float) -> None:
        self.r = r
        self.p = p
        self.y = y
        self.r_value_label.config(text=f"{r:7.2f}")
        self.p_value_label.config(text=f"{p:7.2f}")
        self.y_value_label.config(text=f"{y:7.2f}")

    def get_angle(self) -> Tuple[float]:
        return self.r, self.p, self.y

class App(tk.Tk):
    """ GUIの表示用のオブジェクト
    """
    def __init__(self):
        super().__init__()
        self.geometry("+0+0")

        self.canvas = canvas_gui.ImageCanvas(self)
        self.canvas.pack()

        # angle_info 
        self.info_angle = AngleFrame(self)
        self.info_angle.pack()

        # button configure 
        buttons = tk.Frame(self)
        buttons.pack()
        self.button_start = tk.Button(buttons, text="start", command=self.start)
        self.button_start.pack(side="left")
        self.button_exit = tk.Button(buttons, text="exit", command=self.exit)
        self.button_exit.pack(side="left")

        self.after_id = None
        self.r_queue = multiprocessing.Queue()
        self.s_queue = multiprocessing.Queue()
        self.p = multiprocessing.Process(
            target=detection_object, args=(self.s_queue, self.r_queue), daemon=True,
        )
        """
        self.parent_pipe, self.child_pipe = multiprocessing.Pipe()
        self.p = multiprocessing.Process(
            target=detection_object_with_pipe, args=(self.child_pipe, ), daemon=True,
        )
        """
        self.p.start()
        self.first_flag = True
        self.text = None
        self.objs = None

    def start(self):
        """ キャンバスの更新開始ボタン
        """
        self.button_start.config(state="disable")
        self.update_canvas()

    def exit(self):
        """ GUIの終了関数
        """
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        # self.parent_pipe.close()
        self.destroy()

    def update_frames(self) -> np.ndarray:
        """カメラの更新関数
        """
        camera.update_frames()
        color_image = camera.get_color_image()
        return color_image

    def update_canvas(self):
        """ キャンバスのアップデート関数
        """
        #image = np.ones((480, 640, 3)) * next(self.color_gen)
        image = self.update_frames()
        r, p, y = camera.get_camera_angles()
        self.info_angle.set_angle(r, p, y)
        if self.first_flag:
            self.s_queue.put(image)
            #self.parent_pipe.send(image)
            self.start_time = time.time()
            self.first_flag = False
        # queue 処理
        if not self.r_queue.empty():
            detection_result = self.r_queue.get()
            #self.text = str(detection_result)
            self.objs = detection_result
            elapsed_time = time.time() - self.start_time
            print("Elapsed_Time")
            print(f"\ttype:detection\telapsed_time:{elapsed_time:.4f}")
            self.s_queue.put(image)
            self.start_time = time.time()
        """
        # pipe 処理
        if self.parent_pipe.poll():
            detection_result = self.parent_pipe.recv()
            #self.text = str(detection_result)
            self.objs = detection_result
            elapsed_time = time.time() - self.start_time
            print("Elapsed_Time")
            print(f"\ttype:detection\telapsed_time:{elapsed_time:.4f}")
            self.parent_pipe.send(image)
            self.start_time = time.time()
        """
        
        if self.text is not None:
            height, width = image.shape[:2]
            result = cv2.putText(
                image.copy(), f"RESULT:{str(self.text)}", (height // 4 , width // 4), cv2.FONT_HERSHEY_SIMPLEX,
                1, [255, 255, 255], thickness=0
            )

        if self.objs is not None:
            draw_start_time = time.time()
            height, width = image.shape[:2]
            result = draw.draw_objects(image.copy(), self.objs)
            draw_elapsed_time = time.time() - draw_start_time
            #print(f"type:drawing\telapsed_time:{draw_elapsed_time:.4f}")
        else:
            result = image.copy()
        self.canvas.create_color_canvas(result.astype("uint8"))
        self.after_id = self.after(10, self.update_canvas)

def main():
    """ main
    """
    try:
        camera.start()
    except Exception as e:
        raise e
    else:
        try:
            app = App()
            app.mainloop()
        finally:
            camera.stop()

if __name__ == "__main__":
    main()
