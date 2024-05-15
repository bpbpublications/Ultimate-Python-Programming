fruits_prices = {'apple': 100, 'banana':75, 'mango':80}

x = fruits_prices.setdefault('apple',0)
y = fruits_prices.setdefault('grapes',0)

print(x, y)
