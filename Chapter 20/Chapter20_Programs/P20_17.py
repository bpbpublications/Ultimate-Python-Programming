numbers = [23, 45, 67]
try:
    print(numbers[3])
except LookupError as e:
    print(type(e))
    print(e.args)
    print(e)
