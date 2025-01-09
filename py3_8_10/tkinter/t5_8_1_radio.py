""" radioボタンを配置
ラジオボタンの定義は複数の選択肢から一つだけ選択する際に使用されるボタンである。
"""

import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()

    radio_button_1 = tk.Radiobutton(root, text="radio 1")
    radio_button_1.pack()
    radio_button_2 = tk.Radiobutton(root, text="radio 2")
    radio_button_2.pack()
    radio_button_3 = tk.Radiobutton(root, text="radio 3")
    radio_button_3.pack()

    root.mainloop()
