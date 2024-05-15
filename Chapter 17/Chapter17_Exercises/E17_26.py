class Factorial:
    def __init__(self, high):
        self.high = high

    def __iter__(self):
        return FactorialIterator(self)


class FactorialIterator:
    def __init__(self, source):
        self.source = source
        self.n = 1
        self.fact = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.source.high:
            raise StopIteration
        self.fact = self.fact * self.n
        self.n += 1

        return self.fact


x = Factorial(7)

for i in x:
    print(i)

for i in x:
    print(i)