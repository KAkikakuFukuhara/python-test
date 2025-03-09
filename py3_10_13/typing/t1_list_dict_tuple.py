### pythonn 3.9?で必要なくなった
### 後置サポート？いまところ3.13までは確認済み
from typing import List, Dict, Tuple


def get_list() -> List[int]:
    return [1, 2]


def get_dict() -> Dict[int, int]:
    return {1:1}


def get_tuple() -> Tuple[int, int]:
    return (1, 1)



x: List[int] = get_list()
y: Dict[int, int] = get_dict()
z: Tuple[int, int] = get_tuple()
