import json

with open("./test.json", "r") as f:
    data = json.load(f)

print(data['share']['anc_ratios'])