import sys
import pprint

print(__package__)
print(__name__)

if __package__ is None:
    from pkgs.test_pkg import test_pkg
    from lib.dataloader import DataLoader
else:
    from .pkgs.test_pkg import test_pkg
    from .lib.dataloader import DataLoader

x = test_pkg.utils.mydataclasses.A()
y = DataLoader()

print(x)
print(y)

import os
file_dir = os.path.abspath(os.path.dirname(__file__))
z = y.load_data(f"{file_dir}/../data/test.txt")
print(z)
z.print()

pprint.pprint(sys.modules)