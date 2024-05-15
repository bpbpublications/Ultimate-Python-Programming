fruits = {'apple', 'banana', 'grapes'}
veggies = {'potato', 'onion', 'cabbage'}
stationery = {'pencil', 'eraser', 'sharpener', 'marker'}
prices = {'pencil': 10, 'eraser': 5, 'sharpener': 4, 'marker': 20, 'potato': 30,
          'onion': 25, 'cabbage': 22, 'apple': 90, 'banana': 60, 'grapes': 80}

for thing in prices:
    if thing in fruits:
        continue
    prices[thing] += 0.1 * prices[thing]
print(prices)

prices = {'pencil': 10, 'eraser': 5, 'sharpener': 4, 'marker': 20, 'potato': 30,
          'onion': 25, 'cabbage': 22, 'apple': 90, 'banana': 60, 'grapes': 80}
for thing in prices:
    if thing not in fruits:
        prices[thing] += 0.1 * prices[thing]
print(prices)
