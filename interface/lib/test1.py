import random

class Target:
    def __init__(self, x:float, y:float):
        self.a:float = x
        self.b:float = y


class Predictor:
    def __init__(self, name:str):
        self.name = name

    def predict(self) -> Target:
        target:Target = Target(
            random.random(),
            random.random()
        )
        return target
