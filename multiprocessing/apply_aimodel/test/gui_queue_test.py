import multiprocessing
import tkinter as tk
from typing import List, Tuple
import random
import time

import numpy as np
import cv2
import tensorflow as tf

from app_module import canvas_gui
from app_module import draw

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

def make_model() -> tf.keras.Model:
    """ AIモデルを作成
    """
    input_layer = tf.keras.layers.Input(shape=(480, 640, 3), name="input")
    x = tf.keras.layers.Conv2D(8, 3, activation='relu', padding="same", name="conv1_1")(input_layer)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv1_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv1_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv2_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_1")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_2")(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding="same", name="conv3_3")(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(4, 4), name="pool3")(x)
    x = tf.keras.layers.Flatten(name="flatten")(x)
    x = tf.keras.layers.Dense(512, activation="relu", name="linear1")(x)
    x = tf.keras.layers.Dense(10, activation="softmax", name="linear2")(x)

    model = tf.keras.Model(inputs=input_layer, outputs=x)
    model.summary()

    return model

def make_random_rect(height:int=480, width:int=640) -> Tuple[int]:
    """ ランダムな矩形を作成
    """
    rect_w = random.randint(0, width - int(width / 4))
    rect_e = random.randint(rect_w, width-1)
    rect_n = random.randint(0, height - int(height / 4))
    rect_s = random.randint(rect_n, height-1)

    return rect_n, rect_w, rect_s, rect_e

names = ['apple', 'orange', 'banana', 'greap', 'tomato', 'poteto']
def make_random_obj(height=480, width=640, obj_num=1) -> List[dict]:
    """　ランダムなオブジェクトを生成
    """
    objs = []
    for i in range(obj_num):
        name = names[random.randint(0, len(names)-1)]
        rect_n = random.randint(0, height // 2)
        rect_w = random.randint(0, width // 2)
        rect_s = random.randint(rect_n, height-1)
        rect_e = random.randint(rect_w, width-1)
        prob = random.random()
        c_w = (rect_e - rect_w) // 2 + rect_w
        c_h = (rect_s - rect_n) // 2 + rect_n
        obj = Object(name, (rect_w, rect_n), (rect_e, rect_s), prob, c_w, c_h)
        objs.append(obj)
    return objs

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

def detection_object(r_queue:multiprocessing.Queue, s_queue:multiprocessing.Queue) -> None:
    """ 物体検出を行う処理（今回は単純に物体の確率を出力するだけ）
    """
    start_time = time.time()
    model = make_model()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            break

        if r_queue.empty():
            continue

        image = r_queue.get()
        image = np.expand_dims(image, 0).astype("float32") / 255
        result = model(image, training=True)
        args = tf.keras.backend.argmax(result).numpy()
        objs = make_random_obj(obj_num=random.randint(1, 4))
        s_queue.put(objs)

def color_generator():
    """ 順番に色を作成するジェネレーター
    """
    red = [128, 0, 0]
    green = [0, 128, 0]
    bleu = [0, 0, 128]
    yellow = [128, 128, 0]
    cyan = [0, 128, 128]
    magenta = [128, 0, 128]
    color_list = [red, green, bleu, yellow, cyan, magenta]

    """
    # 濃淡カラーを出力
    a1 = [0 for i in range(3)]
    a2 = [1*(2**4) for i in range(3)]
    a3 = [2*(2**4) for i in range(3)]
    a4 = [3*(2**4) for i in range(3)]
    a5 = [4*(2**4) for i in range(3)]
    a6 = [5*(2**4) for i in range(3)]
    a7 = [6*(2**4) for i in range(3)]
    a8 = [7*(2**4) for i in range(3)]
    color_list = [a1, a2, a3, a4, a5, a6, a7, a8]
    """

    while True:
        for color in color_list:
            yield color

class App(tk.Tk):
    """ GUIの表示用のオブジェクト
    """
    def __init__(self):
        super().__init__()
        self.geometry("+0+0")

        self.canvas = canvas_gui.ImageCanvas(self)
        self.canvas.pack()
        self.button_start = tk.Button(self, text="start", command=self.start)
        self.button_start.pack()
        self.button_exit = tk.Button(self, text="exit", command=self.exit)
        self.button_exit.pack()

        self.after_id = None
        self.color_gen = color_generator()

        self.r_queue = multiprocessing.Queue()
        self.s_queue = multiprocessing.Queue()
        self.p = multiprocessing.Process(
            target=detection_object, args=(self.s_queue, self.r_queue), daemon=True,
        )
        self.p.start()
        self.first_flag = True
        self.text = None
        self.objs = None

    def start(self):
        """ キャンバスの更新開始ボタン
        """
        self.button_start.config(state="disable")
        self.update_frames()

    def exit(self):
        """ GUIの終了関数
        """
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        self.destroy()

    def update_frames(self):
        """ キャンバスのアップデート関数
        """
        image = np.ones((480, 640, 3)) * next(self.color_gen)
        if self.first_flag:
            self.s_queue.put(image)
            self.start_time = time.time()
            self.first_flag = False

        if not self.r_queue.empty():
            detection_result = self.r_queue.get()
            #self.text = str(detection_result)
            self.objs = detection_result
            elapsed_time = time.time() - self.start_time
            print(f"type:detection\telapsed_time:{elapsed_time:.4f}")
            self.s_queue.put(image)
            self.start_time = time.time()

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
        self.after_id = self.after(10, self.update_frames)

def main():
    """ main
    """
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()