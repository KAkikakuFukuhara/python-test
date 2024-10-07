from libs.config import Config as BaseConfig

class Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.a = 11
        self.b = 12
