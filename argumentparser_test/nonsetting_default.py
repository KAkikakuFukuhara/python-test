""" デフォルトに何も設定しなかった場合は値はどうなるのか実験
"""
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--src_dir", type=str, default="./")
    parser.add_argument("--out_dir",  type=str)
    args = parser.parse_args()
    print(type(args.src_dir)) # str
    print(type(args.out_dir)) # NoneType
