from . import test2
if len(__package__.split(".")) == 1:
    from utils import config
else:
    from ..utils import config

x = config.Config()