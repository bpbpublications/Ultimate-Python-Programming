data = [1, 2, 3.4, 6, 'd', 8, 7, 9.8, 'Python']
integers = [x for x in data if type(x) == int]
floats = [x for x in data if type(x) == float]
strings = [x for x in data if type(x) == str]
print(integers, floats, strings)

