"""
aaaaa
"""
import sys
import pprint

import project1.src as project1
pprint.pprint(sys.modules)
from utils import classA
pprint.pprint(sys.modules)
from project1.src import classB
pprint.pprint(sys.modules)
