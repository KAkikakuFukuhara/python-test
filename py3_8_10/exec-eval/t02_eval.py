""" eval
"""

if __name__ == "__main__":
    ### evalはbool値を返す
    x = 1
    res = eval("x==1")
    print(res)
    res = eval("x==0")
    print(res)


    ### 反復で変数を評価できる
    hoge0 = 0
    hoge1 = "1"
    hoge2 = 2.0
    name_and_type_pairs = [
        ("hoge0", "int"),
        ("hoge1", "str"),
        ("hoge2", "float")]
    for name, type_ in name_and_type_pairs:
        res = eval(f"isinstance({name}, {type_})")
        print(res)

