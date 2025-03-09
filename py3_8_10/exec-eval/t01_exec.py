""" t01, exec
"""

if __name__ == "__main__":
    ### 実行
    ## ここでx=1を実行
    exec("x=1")
    ## 実行が成功する。execで定義されていることが確認できる
    print(x)

    ### 他の変数を代入
    y = 2
    exec("z=y")
    print(z)

    ### 文字列の変数名を作成
    var_name = "test"
    exec(f"{var_name}=3")
    print(test)

    ### 変数名の加工
    var_base_name = "hoge"
    for i in range(3):
        exec(f"{var_base_name}{i}={i}")
    print(f"hoge0= {hoge0}")
    print(f"hoge1= {hoge1}")
    print(f"hoge2= {hoge2}")


    ### クラスにまとめて代入
    class Hoge:
        def __init__(self):
            self._x = 0
            self._y = 0
            self._z = 0

        def update(self, x, y, z):
            arg_names = ['x', 'y', 'z']
            for name in arg_names:
                exec(f"self._{name}={name}")


    obj = Hoge()
    obj.update(1, 10, 20)
    print(f"obj._x= {obj._x}")
    print(f"obj._y= {obj._y}")
    print(f"obj._z= {obj._z}")


    ### 失敗すると例外発生
    try:
        exec("x===3")
    except Exception as e:
        print(type(e), e)
