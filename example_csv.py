import json

result = {}

with open('animals.json', mode='r', encoding='utf8') as f:
    d = json.load(f)
    for k, v in d.items():
        result[k] = v[1] - v[0]

m = max(result.values())

print([k for k, v in result.items() if v == m])