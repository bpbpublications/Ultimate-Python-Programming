D = {'apple': 210, 'banana': 100, 'grapes': 90, 'mango': 250, 'cherry': 225}

for fruit in D:
    print(fruit, end=' ')
print()

for fruit in D.keys():
    print(fruit, end=' ')
print()

for price in D.values():
    print(price, end=' ')
print()

for pair in D.items():
    print(pair, end=' ')
print()

for fruit, price in D.items():
    print(f'Price of {fruit} is {price}')

print()
for fruit, price in D.items():
    if price > 200:
        print(f'Price of {fruit} is {price}')

print()
for fruit, price in D.items():
    if price > 200:
        D[fruit] -= 0.1 * price

print(D)

