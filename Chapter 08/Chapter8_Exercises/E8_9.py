cities = ['London', 'Paris', 'Noida', 'Perth', 'Rome']
for city in cities:
    if city == 'Paris':
        cities.append('New York')
    if city == 'New York':
        cities.append('New Delhi')
print(cities)
