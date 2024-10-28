class Dir2_1:
    def print(self):
        print("aaaa")

from ..dir1.test_dir1 import Dir1

class Dir2(Dir1):
    def print(self):
        print("bbbb")