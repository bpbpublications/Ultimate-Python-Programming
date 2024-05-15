prices = {'pencil': 10, 'pen': 22, 'eraser': 12, 'sharpener': 13, 'marker': 32}
print(prices['pen'])
print(prices.get('pen'))
print(prices.get('stapler'))
print(prices.get('stapler', 0))
print(prices.get('stapler', 5))

