import sys
import pprint

if __package__ is not None:
    from . import lib
else:
    import lib

pprint.pprint(sys.modules)