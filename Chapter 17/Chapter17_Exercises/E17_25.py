class Squares:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            x = self.current
            self.current += 1
            return x * x


x = Squares(2, 8)

for i in x:
    print(i)

print(sum(x))
