D = {'pen': 10, 'pencil': 5, 'eraser': 8, 'marker': 15, 'ruler': 19}

for fruit, price in D.items():
    print(fruit.ljust(8), price * '-')
