from abc import ABC, abstractmethod

from lib import test1
from lib import test2

class TargetAdapter:
    @classmethod
    def from_test1_target(cls, target:test1.Target) -> 'TargetAdapter':
        return cls(target.a, target.b)


    @classmethod
    def from_test2_target(cls, target:test2.Target) -> 'TargetAdapter':
        return cls(target.c, target.d)


    def __init__(self, x:float=0.0, y:float=0.0):
        self.x:float = x
        self.y:float = y


class PredictorInterface(ABC):
    """インターフェースクラス"""
    @abstractmethod
    def predict(self):
        pass


class Test1Predctor(test1.Predictor, PredictorInterface):
    """多重継承によってインターフェースを含んだモノとなる"""
    def __init__(self, name:str):
        super().__init__(name)


    def predict_all(self) -> TargetAdapter:
        return TargetAdapter.from_test1_target(super().predict())


predictor = Test1Predctor("test1")
x = predictor.predict()
