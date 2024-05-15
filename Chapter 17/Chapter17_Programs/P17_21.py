class Reverse:
    def __init__(self, source):
        self.source = source

    def __iter__(self):
        return ReverseIterator(self.source)


class ReverseIterator():
    def __init__(self, source):
        self.source = source
        self.index = len(self.source)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.source[self.index]


x = Reverse('Knowledge')

for c in x:
    print(c, end=' ')

for c in x:
    print(c, end=' ')
