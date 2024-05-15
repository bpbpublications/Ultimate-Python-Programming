prices = {'pencil': 10, 'pen': 22, 'eraser': 12, 'gum': 13, 'marker': 32, 'ruler': 30}
del prices['marker']
print(prices)

x = prices.pop('pencil')
print(x)

print(prices)

# print(prices.pop('book'))
print(prices.pop('book', 0))

print(prices.popitem())
print(prices)
print(prices.popitem())
print(prices)
prices.clear()
print(prices)

