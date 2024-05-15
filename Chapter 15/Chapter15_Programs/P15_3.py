class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, A):
            return self.value + other.value
        elif isinstance(other, float) or isinstance(other, int):
            return self.value + other
        else:
            return NotImplemented


class B:
    def __init__(self, data):
        self.data = data

    def __radd__(self, other):
        if isinstance(other, A):
            return self.data + other.value
        elif isinstance(other, B):
            return self.data + a.data
        else:
            return NotImplemented


a = A(1)
b = B(2)
print(a + b)
