""" LabelFrame
"""
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    ### LabelFrame
    ## Frameに囲いの線と文字列が追加されたモノ
    ## 使い方はFrameと同じ
    labelframe = tk.LabelFrame(root, text="LabelFrame")
    labelframe.pack()

    ### コンストラクタにlabelframeを渡す
    button = tk.Button(labelframe, text="Button")
    button.pack()

    root.mainloop()