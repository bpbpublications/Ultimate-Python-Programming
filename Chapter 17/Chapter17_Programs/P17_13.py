class Fibonacci:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        if f > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return f


x = Fibonacci(100)

for i in x:
    print(i, end=' ')
print(50 in x, 55 in x)
