class Cubes:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        x = self.current
        self.current += 1
        return x*x*x

x = Cubes(2,8)

for i in x:
    print(i, end = ' ')

print('Sum =',sum(x))
