class Squares:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return SquaresIterator(self)


class SquaresIterator:
    def __init__(self, source):
        self.source = source
        self.current = source.low

    def __next__(self):
        if self.current > self.source.high:
            raise StopIteration
        else:
            x = self.current
            self.current += 1
            return x * x


x = Squares(2, 8)

for i in x:
    print(i)

print(sum(x))
