names = ['Sophia', 'Michael', 'Benedict', 'Anthony']
cities = ['Paris', 'London', 'Bareilly', 'Tokyo']
phones = [676858939, 223878965, 856937891, 676757913]

ids = list(map(lambda x,y,z : x[-2:] + y[:2] + str(z)[:3], names, cities, phones))
print(ids)
