import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties
font_path = "/usr/share/fonts/truetype/migmix/migmix-1m-regular.ttf"
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams["font.family"] = font_prop.get_name()

dir_name = os.path.dirname(__file__)
print(dir_name)
list_dir = os.listdir(dir_name)
txt_files = []
for d in list_dir:
    f_name = d.split(".")
    if len(f_name) < 2:
        continue
    if f_name[-1] == "txt":
        txt_files.append(d)
txt_files.sort()
print(txt_files)

def plot_each():
    for file_path in txt_files:
        with open(f"{dir_name}/{file_path}", "r") as f:
            text = f.read()
        text = text.split("\n")
        time, r, p, y = [], [], [], []
        for t in text:
            line = t.split(",")
            time.append(float(line[1].split(":")[-1]))
            r.append(float(line[2].split(":")[-1]))
            p.append(float(line[3].split(":")[-1]))
            y.append(float(line[4].split(":")[-1]))


        plt.title(file_path)
        plt.plot(time, r, label="rool")
        plt.plot(time, p, label="pitch")
        plt.ylim(-3.0, 1.0)
        plt.legend()
        plt.show()

def plot_separate():
    rolls, pitchs, yaws, times, names = [], [], [], [], []
    for file_path in txt_files:
        with open(f"{dir_name}/{file_path}", "r") as f:
            text = f.read()
        text = text.split("\n")
        time, r, p, y = [], [], [], []
        for t in text:
            line = t.split(",")
            time.append(float(line[1].split(":")[-1]))
            r.append(float(line[2].split(":")[-1]))
            p.append(float(line[3].split(":")[-1]))
            y.append(float(line[4].split(":")[-1]))
        rolls.append(r)
        pitchs.append(p)
        yaws.append(y)
        times.append(time)
        names.append(file_path.split(".")[0])
    
    markers = [".", "o", "v", "s", "+", "x", "*"]
    plt.title("roll")
    plt.xlabel("時間")
    plt.ylabel("角度")
    names = ["YOLOv3_realtime", "FasterRCNN_realtime", "None"]
    for n, r, t in zip(names, rolls, times):

        plt.plot(t, r, label=n, linewidth=3.0)
        plt.ylim(-3.0, 0.5)
        plt.legend()
    else:
        plt.show()

    plt.title("pitch")
    plt.xlabel("時間")
    plt.ylabel("角度")
    for n, r, t in zip(names, pitchs, times):
        plt.plot(t, r, label=n, linewidth=3.0)
        plt.ylim(0.0, 1.5)
        plt.legend()
    else:
        plt.show()

if __name__ == "__main__":
    plot_separate()
