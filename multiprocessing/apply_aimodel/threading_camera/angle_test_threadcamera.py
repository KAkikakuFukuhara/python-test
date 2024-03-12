""" テンプレート
"""
import tkinter as tk
from queue import Queue 
import multiprocessing
import time

import numpy as np

import thread_camera
import canvas_gui
import detections
import draw

# variables 
LIMIT_TIME = 60

###############################
# ラベルとフォームのセットクラス
###############################
class LabelWithHorm(tk.Frame):
    """ ラベルとフォームのセットのGUIオブジェクト
    """
    def __init__(self, master=None, label_text="None", form_text="None"):
        super().__init__(master)
        self.label = tk.Label(self, text=label_text, anchor="s")
        self.label.pack(fill="x")
        self.form = tk.Entry(self, text=form_text, anchor="s")
        self.form.pack(fill="x")

#################################
# カメラの角度表示クラス
#################################
class AngleFrame(tk.Frame):
    """ カメラ角度のGUI
    """
    def __init__(self, master=None):
        super().__init__(master)
        # attribute definition
        self.r = None
        self.p = None
        self.y = None

        # widget definition
        none_text = " " * 2 + "None,"
        r_label = tk.Label(self, text="R:")
        p_label = tk.Label(self, text="P:")
        y_label = tk.Label(self, text="Y:")
        self.r_value_label = tk.Label(self, text=none_text)
        self.p_value_label = tk.Label(self, text=none_text)
        self.y_value_label = tk.Label(self, text=none_text)

        # widget pack        
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


#########################
# GUIの本体
#########################
class App(tk.Tk):
    """ アプリ
    """
    def __init__(self, 
                 camera_queue:Queue, 
                 image_queue:multiprocessing.Queue, 
                 result_queue:multiprocessing.Queue):

        super().__init__()
        # tkinter after event id 
        self.after_id =None

        # thread queue
        self.input_queue = camera_queue

        # multiprocessing configure
        self.image_queue = image_queue
        self.result_queue = result_queue
        self.objs = None

        # detection configure
        self.detection_flag = False
        self.is_run_detection = False

        # angle configure
        self.anglelist = []

        # test configure
        self.first_flag = True

        self.set_widget()


    def set_widget(self):
        """ set widget for app
        """
        # canvas congiure
        self.canvas = canvas_gui.ImageCanvas(self)
        self.canvas.pack()

        # info configure
        self.angles_info  = AngleFrame(self)
        self.angles_info.pack()

        # buttons configure
        button_frame = tk.Frame(self)
        button_frame.pack()
        self.start_button = tk.Button(button_frame, text="start", command=self.start)
        self.detection_button = tk.Button(button_frame, text="detect", command=self.on_detection_flag)
        self.exit__button = tk.Button(button_frame, text="exit", command=self.exit)

        ## butttons pack
        self.start_button.pack(side="left")
        self.detection_button.pack(side="left")
        self.exit__button.pack(side="left")

    def start(self):
        """ start update
        """
        self.start_button.config(state="disable")
        self.app_start_time = time.time()
        self.after_id = self.after(10, self.update)

    def exit(self):
        """ exit App
        """
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            with open("therad_camera.txt", "w") as f:
                text = "\n".join(self.anglelist)
                f.write(text)
        self.destroy()

    def update_data(self):
        data = self.input_queue.get()
        self.roll, self.pitch, self.yaw = angles = data[0]
        self.color_frame = data[1]
        self.depth_frame = data[2]        

    def get_angles(self) -> tuple:
        return self.roll, self.pitch, self.yaw

    def get_color_image(self) -> np.ndarray:
        return np.asanyarray(self.color_frame.get_data())

    def get_depth_image(self) -> np.ndarray:
        return np.asanyarray(self.depth_frame.get_data())

    def update(self):
        """ update gui
        """
        if not self.input_queue.empty():
            update_start_time = time.time()
            self.update_data()
            angles = self.get_angles()
            color_image = self.get_color_image()
            depth_image = self.get_depth_image()

            if self.detection_flag:
                if not self.is_run_detection:
                    self.image_queue.put(color_image)
                    self.is_run_detection = not self.is_run_detection
                
                if not result_queue.empty():
                    self.objs = result_queue.get()
                    self.is_run_detection = not self.is_run_detection

                if self.objs is not None:
                    color_image = draw.draw_objects(color_image, self.objs)
                    pass

            self.canvas.create_color_canvas(color_image)
            self.angles_info.set_angle(angles[0], angles[1], angles[2])
            app_elapsed_time = time.time() - self.app_start_time
                
            text_data = f"Elapsed_time:{app_elapsed_time:.4f}, R:{self.roll:7.2f}, P:{self.pitch:7.2f}, Y:{self.yaw:7.2f}"
            self.anglelist.append(text_data)

            if app_elapsed_time > 10 and self.first_flag:
                self.first_flag = False
                self.on_detection_flag()

            if app_elapsed_time > LIMIT_TIME:
                self.exit()
            
        self.after_id = self.after(10, self.update)

    def on_detection_flag(self):
        self.detection_flag = not self.detection_flag
        
if __name__ == "__main__":
    # camera setting
    data_queue = Queue()
    camera = thread_camera.ThreadCamera(data_queue)
    # detection process setting
    image_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=detections.detect, args=(image_queue, result_queue, ), daemon=True)
    p.start()

    app = App(data_queue, image_queue, result_queue)
    camera.start()

    try:
        app.mainloop()
    finally:
        camera.set_exit_flag()
        camera.join()