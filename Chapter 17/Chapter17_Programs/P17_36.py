class Fibonacci:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        a = 0
        b = 1
        while a < self.max:
            yield a
            a, b = b, a + b


x = Fibonacci(100)

for i in x:
    print(i, end=' ')

for i in x:
    print(i, end=' ')
