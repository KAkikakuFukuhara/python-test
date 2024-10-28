""" Buttonにバインドされた関数に渡される引数の表示
"""
import tkinter as tk

def callback(*args):
    """ 左クリック：引数は何か表示
    """
    print("--- Left Button Pushed ---")
    for arg in args:
        print(type(arg), arg)


def callback2(event: tk.Event):
    """ 右クリック：
    引数がイベントクラスなのが分かったのでクラスのプロパティを表示
    """
    print("--- Right Button Pushed ---")
    for e in dir(event):
        if "__" not in e:
            ### 変数名：変数の型：値　の形式で表示する
            print("{}: {}: {}".format(e, eval(f"type(event.{e})"), eval(f"event.{e}")))
            ### eval(str)は strのプログラムを実行して結果を返す


if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="button")
    button.pack()

    button.bind("<Button-1>", func=callback)
    button.bind("<Button-3>", func=callback2)

    root.mainloop()