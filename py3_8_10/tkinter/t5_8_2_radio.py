""" radioボタン:実際に機能させてみる
"""

import tkinter as tk


def write_label_from_raido_value(evnet: tk.Event):
    ### 値の取得
    value = selected_var.get()
    ### ラベルの更新
    label['text'] = f"value = {value}"


if __name__ == "__main__":
    root = tk.Tk()

    ### 複数のラジオボタンが値を参照する共通オブジェクト
    selected_var = tk.IntVar(value=1)

    radio_button_1 = tk.Radiobutton(root, text="radio 1", variable=selected_var, value=1)
    radio_button_2 = tk.Radiobutton(root, text="radio 2", variable=selected_var, value=2)
    radio_button_3 = tk.Radiobutton(root, text="radio 3", variable=selected_var, value=3)
    radio_button_1.pack()
    radio_button_2.pack()
    radio_button_3.pack()

    ### 値の取得と表示用のウィジェット
    button = tk.Button(root, text="show selected value")
    button.bind("<Button-1>", write_label_from_raido_value)
    button.pack()
    label = tk.Label(root, text="value = N")
    label.pack()

    root.mainloop()
