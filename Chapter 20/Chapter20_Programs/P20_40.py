class MyError(Exception):
    def __init__(self, x, y):
        self.data = x
        self.value = y

    def __str__(self):
        return f'Exception of type MyError raised, {self.data}, {self.value}'


try:
    raise MyError(23, 45)
except MyError as e:
    print(e)
    print(e.data, e.value)
