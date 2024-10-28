import os
import sys
import pprint

file_dir = os.path.abspath(os.path.dirname(__file__))
new_paths = []
new_paths.append(file_dir)
for path in new_paths:
    if path not in sys.path:
        sys.path.insert(0, path)

pprint.pprint(sys.path)

from utils import classB
print(classB)

