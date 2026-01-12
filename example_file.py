import os

res = []

for root, _, files in os.walk("img"):
    for file in files:
        res.append((os.path.getsize(os.path.join(root, file)), file))

print(sorted(res))
for size, name in sorted(res):
    print(name, size)