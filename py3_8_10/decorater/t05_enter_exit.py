""" デコレータにインスタンス変数を渡して __enter__ and __exit__ みたいにする
"""
class Button:
    def __init__(self, text):
        self.text = text


    def on(self):
        print(f"{self.text} on")


    def off(self):
        print(f"{self.text} off")


def deco_maker(button: Button):
    def deco(func):
        def wrapper(*args, **kwargs):
            button.on()
            func(*args, **kwargs)
            button.off()
        return wrapper
    return deco


class Widget:
    def __init__(self):
        self.button1 = Button("button1")
        self.button2 = Button("button1")
        ### 関数の上書きでデコレータを付加する
        ## 参考:https://stackoverflow.com/questions/1231950/how-can-i-use-a-class-instance-variable-as-an-argument-for-a-method-decorator-in
        self.func1 = deco_maker(self.button1)(self.func1)
        self.func2 = deco_maker(self.button2)(self.func2)


    ### selfを渡したデコレータ
    # @deco_maker(self.button1) # selfが参照できないためダメ
    def func1(self, x):
        print(x)


    def func2(self, x):
        print(x)


if __name__ == "__main__":
    w = Widget()
    w.func1("hello")
    w.func2("High")
