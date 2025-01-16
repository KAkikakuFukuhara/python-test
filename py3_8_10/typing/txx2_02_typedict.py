from typing import TypedDict

class ITestRequired(TypedDict):
    x: float
    y: float
    z: float


class Itest(ITestRequired, total=False):
    px: int
    py: int


a: Itest = {"x":1.0, "y":2.0, "z":3.0}
a["x"] # インテリセンスあり、アラートなし
a["px"] # インテリセンスあり、アラートあり
## コッチの方法でアクセスしよう
x = a.get("px") # インテリセンスあり、アラートなし
