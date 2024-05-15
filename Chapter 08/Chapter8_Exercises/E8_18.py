D = {'apple': 210, 'banana': 100, 'grapes': 90, 'mango': 250, 'cherry': 225, 'guava': 80}
for fruit in reversed(sorted(D.keys())):
    print(fruit, D[fruit])
