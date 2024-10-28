"""[summary]
    argparserのargに２つを利用した際に、
    argparserをvarsした辞書型のキーはどうなるかの調査。
    結果:長い方のテキストがキーとなる。
"""

from argparse import ArgumentParser
import pprint

parser = ArgumentParser()
parser.add_argument("-t", "--test", type=int)
args = vars(parser.parse_args())

pprint.pprint(args)