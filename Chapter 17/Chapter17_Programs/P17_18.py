class Alternate:
    def __init__(self, source):
        self.source = source
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.source):
            raise StopIteration
        item = self.source[self.index]
        self.index = self.index + 2
        return item


L = [1, 2, 3, 4, 5, 6, 7, 8]

for i in Alternate(L):
    print(i, end=' ')

for ch in Alternate('intelligent'):
    print(ch, end=' ')
