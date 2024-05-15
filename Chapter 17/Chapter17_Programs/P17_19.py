class Reverse:
    def __init__(self, source):
        self.source = source
        self.index = len(source)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.source[self.index]


L = [1, 2, 3, 4, 5, 6, 7, 8]

for i in Reverse(L):
    print(i, end=' ')

for ch in Reverse('intelligent'):
    print(ch, end=' ')
