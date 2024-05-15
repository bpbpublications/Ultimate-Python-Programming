class CustomError(Exception):
    def __init__(self, x, y):
        self.data = x
        self.value = y

    def __str__(self):
        return f'CustomError raised, {self.data}, {self.value}'


try:
    raise CustomError(4, 8)
except CustomError as e:
    print(e)
    x, y = e.args
    print(x, y)
    print(e.data, e.value)
