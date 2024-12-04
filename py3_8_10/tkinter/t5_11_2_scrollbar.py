""" scrollbar: Canvasとの連動
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x450")

    ### canvas
    canvas = tk.Canvas(root, height=400, width=400, bg="black")
    canvas.grid(row=0, column=0)

    ### scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

    ### scrollbarとcanvasを連動させる
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    ### スクロール範囲を指定。これが無いと無限にスクロールできる
    canvas.config(scrollregion=(0, -200, 400, 600))
    ### 確認用矩形
    canvas.create_rectangle(100, 100, 300, 300, fill="red")

    root.mainloop()