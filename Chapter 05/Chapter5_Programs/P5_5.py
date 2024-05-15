prices = {'pencil': 10, 'pen': 22, 'eraser': 12, 'sharpener': 13, 'marker': 32}
print(prices.setdefault('pen'))
print(prices.setdefault('stapler') )
print(prices)

prices.setdefault('gum',10)
print(prices)
