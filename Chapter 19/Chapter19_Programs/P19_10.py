d = {'pen': 23, 'eraser': 5, 'book': 30}

print(sorted(d))
print(sorted(d.keys()))
print(sorted(d.values()))
print(sorted(d.items()))
print(sorted(d.items(), key=lambda t: t[1]))
