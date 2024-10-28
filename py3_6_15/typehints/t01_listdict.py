""" py38でのタイプヒントの記載方法の書き方を試す
"""
### 失敗：インポートできない
#from __future__ import annotations

#x:list[int]= [1, 2, 3] # 失敗
pass

### こっちだと問題ない
from typing import List, Dict
x: List[int] = [1, 2, 3]
y: Dict[int ,int] = {1:2}