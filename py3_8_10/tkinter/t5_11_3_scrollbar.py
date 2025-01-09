""" scrollbar: Canvasとの連動（縦+横）
"""
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x450")

    canvas = tk.Canvas(root, height=400, width=400, bg="black")
    canvas.grid(row=0, column=0)

    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
    ## 横スクロールの追加
    scrollbar2 = tk.Scrollbar(root, orient="horizontal")
    scrollbar2.grid(row=1, column=0, sticky=tk.W+tk.E)

    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    ## 今度はX方向に
    scrollbar2.config(command=canvas.xview)
    canvas.config(xscrollcommand=scrollbar2.set)

    canvas.config(scrollregion=(-200, -200, 600, 600))

    ### 確認用矩形
    canvas.create_rectangle(100, 100, 300, 300, fill="red")

    root.mainloop()