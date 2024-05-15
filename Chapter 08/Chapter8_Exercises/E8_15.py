names = ['Sam', 'Tom', 'Bob', 'Rob']
ages = [23, 32, 25, 30]
cities = ['Paris', 'London', 'Tokyo', 'Paris']
for data in zip(names, ages, cities):
    name, age, city = data
    if age > 25:
        print(name, city, end=' ')
