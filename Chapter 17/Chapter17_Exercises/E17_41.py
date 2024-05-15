class Triplets:
    def __init__(self, data):
        self.data = data
        self.len = len(data)
        self.first = 0
        self.second = 1
        self.third = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.first == self.len or self.second == self.len or self.third == self.len:
            raise StopIteration
        t = (self.data[self.first], self.data[self.second], self.data[self.third])
        self.first += 3
        self.second += 3
        self.third += 3
        return t


L = [21, 33, 65, 18, 81, 24, 46, 68, 79, 89, 90, 91]
x = Triplets(L)
for i in x:
    print(i)

names = ['Raj', 'Dev', 'Sam', 'Pam', 'Tom', 'Ram', 'Kim', 'Rob', 'Sim', 'Tim']
for i in Triplets(names):
    print(i)
