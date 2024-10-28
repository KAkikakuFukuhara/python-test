import pyrealsense2 as rs
import numpy as np
import time
import tkinter as tk
import canvas_gui
import threadcameras

max_threshold = 100.0 # 距離の閾値（m) 上限
min_threshold = 0.0 # 距離の閾値（m) 下限

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.camera = threadcameras.ThreadCamera()

        canvas_0x0 = tk.LabelFrame(self, text="COLOR")
        canvas_0x0.grid(row=0, column=0)
        canvas_0x1 = tk.LabelFrame(self, text="DEPTH")
        canvas_0x1.grid(row=0, column=1)
        canvas_1x0 = tk.LabelFrame(self, text="COMPOSE")
        canvas_1x0.grid(row=1, column=0)

        self.color_canvas = canvas_gui.ImageCanvas(canvas_0x0)
        self.color_canvas.pack()
        self.depth_canvas = canvas_gui.ImageCanvas(canvas_1x0)
        # GUIの表示が縦に長い場合はこの下の１行をコメントアウトする
        self.depth_canvas.pack()
        self.compose_canvas = canvas_gui.ImageCanvas(canvas_0x1)
        self.compose_canvas.pack()


        buttons = tk.LabelFrame(self, text="Buttons")
        buttons.grid(row=1, column=1)
        button_start = tk.Button(buttons, text="start", command=self.start)
        button_start.grid(row=0, column=0)
        button_stop = tk.Button(buttons, text="stop", command=self.stop)
        button_stop.grid(row=0, column=1)
        button_exit = tk.Button(buttons, text="EXIT", bg="red", command=self.exit)
        button_exit.grid(row=0, column=3)
        self.after_id = None


    def update_frame(self):
        #self.camera.update_frames()
        threadcameras.frame_lock.acquire()
        frames = self.camera.get_frames()
        threadcameras.frame_lock.release()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())
        return color_image, depth_image

    def update_canvas(self):
        threadcameras.elaped_lock.acquire()
        print(f"経過時間：{self.camera.elapsed_time:3.4f}\t", end="")
        threadcameras.elaped_lock.release()
        threadcameras.angle_lock.acquire()
        roll, pitch, yaw = self.camera.get_camera_angles()
        threadcameras.angle_lock.release()
        print(f"Roll:{roll:7.2f}, Pitch:{pitch:7.2f}, Yaw:{yaw:7.2f}")
        color_image, depth_image = self.update_frame()
        height = depth_image.shape[0]
        width = depth_image.shape[1]
        zeros = np.zeros((height, width)).astype("uint16")
        max_depth = max_threshold / self.camera.depth_scale
        min_depth = min_threshold / self.camera.depth_scale
        depth_image = np.where(np.logical_and(min_depth < depth_image, depth_image < max_depth), depth_image, zeros)
        self.color_canvas.create_color_canvas(color_image)
        self.depth_canvas.create_depth_canvas(depth_image)
        self.compose_canvas.create_compose_canvas(color_image, depth_image)
        self.after_id = self.after(10, self.update_canvas)

    def start(self):
        if self.after_id is None:
            print("start streaming")
            self.update_canvas()
            

    def stop(self):
        if self.after_id is not None:
            print("stop streaming")
            self.after_cancel(self.after_id)
            self.after_id = None

    def exit(self):
        print("program exit")
        self.master.destroy()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mainframe = MainFrame(self)
        self.mainframe.pack()

    def start(self):
        self.mainframe.camera.start()
        try:
            self.mainloop()
        finally:
            threadcameras.flag_lock.acquire()
            threadcameras.flag = False
            threadcameras.flag_lock.release()


if __name__ == "__main__":
    app = App()
    app.start()



