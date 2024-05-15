class PowerTwo:
    def __init__(self, max=1):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


x = PowerTwo(5)
for i in x:
    print(i, end=" ")
print()
print(sum(x))
