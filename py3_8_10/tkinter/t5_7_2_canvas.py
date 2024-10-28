""" Canvas:描画オブジェクトの削除
"""
import tkinter as tk


def delete_object(*args):
    if len(ids) == 0:
        return

    id_ = ids.pop(-1)
    canvas.delete(id_)


if __name__ == "__main__":
    root = tk.Tk()

    width = 640
    height = 480
    bg_color = 'white' # background color
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()

    ### 描画オブジェクトのIDリスト
    ids = []

    ### ボックスの作成
    ## 描画オブジェクトはIDを持っている
    id_ = canvas.create_rectangle(10, 10, 110, 110)
    ids.append(id_)
    id_ = canvas.create_rectangle(30, 30, 90, 90, outline="red")
    ids.append(id_)
    id_ = canvas.create_rectangle(50, 50, 70, 70, fill="#ff00ff")
    ids.append(id_)

    ### オブジェクトの削除ボタン
    button = tk.Button(root, text="delete")
    button.pack()
    button.bind("<Button-1>", delete_object)

    root.mainloop()
