names = ['Amit', 'John', 'Mark', 'Raj']
salaries = [2000, 3000, 2500, 3200]
cities = ['Delhi', 'Chennai', 'Delhi', 'Bangalore']
for name, city, salary in zip(names, cities, salaries):
    print(f'{name} posted in {city} with {salary}')

for i in range(len(names)):
    if cities[i] == 'Delhi':
        salaries[i] += 1000
print(salaries)