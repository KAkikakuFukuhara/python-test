""" ボタンを押すと処理が実行
"""
import tkinter as tk


def callback(*args):
    """ ここに書いた処理が実行される
    引数に値が渡されるので*argsにする
    なお今回は引数を利用しない
    """
    print("!!! Button pushed !!!")



if __name__ == "__main__":
    root = tk.Tk()

    button = tk.Button(root, text="This is Button")
    button.pack()
    ### 以下の形式でボタンに処理を付与
    ### button.bind(sequence, func=func)
    ### ボタンには色々なイベントが存在する(押された・離れたなど)
    ### 今回はボタンが押された際という条件にする
    button.bind("<Button-1>", func=callback)
    ### その他のイベントなどは以下を参考
    ### https://www.rouge.gr.jp/~fuku/tips/python-tkinter/bind.shtml

    root.mainloop()
