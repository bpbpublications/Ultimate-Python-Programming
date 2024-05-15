def calculate(a1, a2, fn):
    fn(a1, a2)

calculate(5, 3, lambda x, y: print(x + y))

calculate(5, 3, lambda x, y: print(2 * x - y))

def func(x, y):
    print(2 * x - y)

calculate(5, 3, func)

def add(a, b):
    print(a + b)

calculate(2, 4, add)
