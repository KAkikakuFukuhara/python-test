"""
    [summary]:
    argparsernの速度チェック
    重たいライブラリの読み込みが発生する前にargparserを実行
    結果：読み込み前の方が早い
"""

import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", default="test")
args = parser.parse_args()
print(args['test'])

import tensorflow