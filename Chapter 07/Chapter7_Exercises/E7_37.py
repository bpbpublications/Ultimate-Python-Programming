D = {'apple': 100, 'grapes': 55, 'banana': 200,  'guava': 60}

for key, value in D.items():
    D[key] = D[key] + 10 if value < 100 else D[key] - 10
print(D)
