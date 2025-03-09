from typing import TypedDict


TestDict = TypedDict(
    "TestDict",
    {
        "x":float,
        "y":float,
        "z":float,
    }
)

class TestDict2(TypedDict):
    x: float
    y: float
    z: float


a: TestDict = {"x":1.0, "y":2.0, "z":3.0}
b: TestDict2 = {"x":1.0, "y":2.0, "z":3.0}
### 以下のインテリセンスが発動
## a['x']
## b['x']
