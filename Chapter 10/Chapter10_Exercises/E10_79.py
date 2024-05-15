def func(*args):
    return [arg[::-1] for arg in args]


L = func('yes', 'no', 'test')
print(L)
