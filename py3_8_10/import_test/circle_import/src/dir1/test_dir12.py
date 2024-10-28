from ..dir2.test_dir2 import Dir2_1
print(Dir2_1)
from ..dir2.test_dir2 import Dir2

class Dir3(Dir2):
    def print(self):
        print("dir3")