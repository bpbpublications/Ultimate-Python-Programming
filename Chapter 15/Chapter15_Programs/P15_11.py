class MyClass:
    def __init__(self, data):
        self.data = data

    def __call__(self, x):
        return self.data + x


obj = MyClass(5)
x = obj(2)
print(x)
