d = {'Ram': 67, 'Sam': 60, 'Tom': 62}

d1 = dict(map(lambda name, h: (name, h * 2.54), d.keys(), d.values()))
print(d1)
