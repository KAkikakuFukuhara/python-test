import sys
import pprint

if __package__ is not None:
    from .pkgs.test_pkg import test_pkg
else:
    from pkgs.test_pkg import test_pkg

pprint.pprint(sys.modules)