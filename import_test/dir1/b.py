from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from myclass import A

import a

class B:
    def __init__(self, a:A):
        self.a = a

if __name__ == "__main__":
    x = B(a.A())
    print(x.a.name)
    