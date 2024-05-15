L = []
for item in dir(str):
    if item.startswith('is'):
        L.append(item)
print(L)
