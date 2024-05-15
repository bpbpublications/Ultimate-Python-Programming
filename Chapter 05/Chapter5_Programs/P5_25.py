cities = {'Cairo', 'Mumbai', 'Agra', 'Bengaluru', 'Rome', 'Perth', 'Bareilly', 'Bern'}
cities.add('Delhi')
print(cities)

cities.remove('Bern')
print(cities)

# cities.remove('Tokyo')
cities.discard('Tokyo')
print(cities)

city = cities.pop()
print(city)
print(cities)
