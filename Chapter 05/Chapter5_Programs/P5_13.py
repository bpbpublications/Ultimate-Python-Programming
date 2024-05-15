stationery = ['pencil', 'marker', 'eraser', 'sharpener']
prices = dict.fromkeys(stationery, 0)
print(prices)

d1 = dict.fromkeys(stationery)
print(d1)

d2 = dict.fromkeys(range(7))
print(d2)

prices = {}.fromkeys(stationery, 0)
print(prices)
