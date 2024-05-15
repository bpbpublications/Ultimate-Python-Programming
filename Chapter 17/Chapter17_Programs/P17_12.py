# Fibonacci series: 0 1 1 2 3 5 8 13 21 34 55 89
class Fibonacci:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        return FiboIterator(self)


class FiboIterator:
    def __init__(self, source):
        self.source = source
        self.a = 0
        self.b = 1

    def __next__(self):
        f = self.a
        if self.a > self.source.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return f


x = Fibonacci(100)

for i in x:
    print(i, end=' ')
print(55 in x, 50 in x)
