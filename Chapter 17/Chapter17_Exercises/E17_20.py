class Odd:
    def __init__(self, max):
        self.num = 1
        self.max = max

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num > self.max:
            raise StopIteration
        self.num += 2
        return self.num - 2


x = Odd(20)

for i in x:
    print(i, end=' ')

print()
print(sum(x))

for i in x:
    print(i, end=' ')
