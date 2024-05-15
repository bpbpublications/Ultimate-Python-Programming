class Cycle:
    def __init__(self, source):
        self.source = source
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index = (self.index + 1) % (len(self.source))
        return self.source[self.index]


count = 0
for i in Cycle([1, 2, 3]):
    print(i, end=' ')
    count += 1
    if count == 10:
        break
