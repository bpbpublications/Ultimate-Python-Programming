class Cubes:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return CubesIterator(self)


class CubesIterator:
    def __init__(self, source):
        self.source = source
        self.current = source.start

    def __next__(self):
        if self.current > self.source.stop:
            raise StopIteration
        else:
            x = self.current
            self.current += 1
            return x * x * x


x = Cubes(2, 8)

for i in x:
    print(i, end=' ')

print('Sum =', sum(x))
