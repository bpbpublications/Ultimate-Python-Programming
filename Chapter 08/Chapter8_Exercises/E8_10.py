cities = ['Paris', 'Noida', 'Perth', 'Rome', 'London']
for city in cities:
    if len(city) < 5:
        cities.append(city)
print(cities)
