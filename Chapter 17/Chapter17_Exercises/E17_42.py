class AdjacentElements:
    def __init__(self, data, num):
        self.data = data
        self.num = num
        self.len = len(data)
        self.indices = list(range(num))

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.indices:
            if i == self.len:
                raise StopIteration

        L = []
        for i in self.indices:
            L.append(self.data[i])

        self.indices = [i + self.num for i in self.indices]
        return tuple(L)


L = [21, 33, 65, 18, 81, 24, 46, 68, 79, 89, 90, 91, 12, 93, 24, 95]

for i in AdjacentElements(L, 4):
    print(i)

for i in AdjacentElements(L, 3):
    print(i)
