names = ['Ted', 'Sam', 'Rob']
cities = ['NY', 'GT', 'UU', 'KK']

n = min(len(names), len(cities))
for i in range(n):
    print(f'{names[i]} will be posted in {cities[i]}')

for name, city in zip(names, cities):
    print(f'{name} will be posted in {city}')
