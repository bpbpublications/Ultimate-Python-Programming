D = {'pen': 10, 'pencil': 5, 'eraser': 8, 'sharpener': None, 'marker': 15, 'ruler': None}

for fruit, price in D.items():
    if price is not None:
        print(fruit.ljust(10, '.'), str(price).rjust(3))
