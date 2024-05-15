class Cubes:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        x = self.current
        self.current += 1
        return x * x * x


x = Cubes(2)

print(next(x))
print(next(x))
print(next(x))

x = Cubes(2)
for i in x:
    if i > 150:
        break
    print(i, end=' ')
