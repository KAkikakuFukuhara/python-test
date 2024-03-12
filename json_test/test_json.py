"""
jsonでは辞書型のキーとして数字を使えない。
上記の検証プログラム。
"""
import json 
import pprint

mapping = {0:"aaaa", 1:"bbbb"}
print("Saving")
pprint.pprint(mapping)

with open("test.json", "w") as f:
    txt = json.dumps(mapping, indent=2)
    f.write(txt)

with open("test.json", "r") as f:
    loaded = json.load(f)

print("Loaded")
pprint.pprint(loaded)
    