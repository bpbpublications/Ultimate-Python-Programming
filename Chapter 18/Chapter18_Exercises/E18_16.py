def add_author(fn):
    fn.author = 'Jack'
    return fn

@add_author
def func1():
    pass

@add_author
def func2():
    pass

print(dir(func1))
print(dir(func1))
