class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        f = self.a
        self.a, self.b = self.b, self.a + self.b
        return f


x = Fibonacci()

n = 0
while n <= 50:
    n = next(x)
    print(n, ' ')
