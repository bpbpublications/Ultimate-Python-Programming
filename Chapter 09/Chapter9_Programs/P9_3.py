cities = ['Belmont', 'New york', 'Paris', 'Buenos aires']
L1 = [city[:3] for city in cities]
print(L1)

L2 = [city.title() for city in cities]
print(L2)

L3 = [(city, len(city)) for city in cities]
print(L3)

L4 = [[city, len(city)] for city in cities]
print(L4)

