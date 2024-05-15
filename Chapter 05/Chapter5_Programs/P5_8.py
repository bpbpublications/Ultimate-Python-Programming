prices = {'pencil': 10, 'pen': 22, 'eraser': 12, 'sharpener': 13, 'marker': 32}
print('pen' in prices)
print('pen' in prices.keys())
print(100 in prices.values())
print(100 not in prices.values())
print(22 in prices.values())
print(('pencil',10) in prices.items())
print(('pencil',12) in prices.items())
