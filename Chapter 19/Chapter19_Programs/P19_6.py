d = {'add': lambda x, y: x + y,
     'subtract': lambda x, y: x - y,
     'multiply': lambda x, y: x * y,
     'divide': lambda x, y: x // y,
     'power': lambda x, y: x ** y,
     'double': lambda x: x * 2,
     'square': lambda x: x ** 2,
     'table': lambda x: [x * i for i in range(1, 11)],
     'summation': lambda x: sum(range(1, x + 1)),
     }
print(d['summation'](4))

print(d['power'](3,2))