prices = {'apple': 210, 'banana': 100, 'grapes': 90, 'mango': 250, 'cherry': 225, 'guava': 80}
for fruit in sorted(prices.keys()):
    print(fruit, prices[fruit], end=' | ')
print()

for fruit, price in sorted(prices.items()):
    print(fruit, price, end=' | ')
print()

for fruit, price in sorted(zip(prices.values(), prices.keys())):
    print(fruit, price, end=' | ')
