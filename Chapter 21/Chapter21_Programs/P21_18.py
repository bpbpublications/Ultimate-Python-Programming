from contextlib import contextmanager


@contextmanager
def manager():
    print('Entering')
    yield
    print('Exiting')


with manager():
    print('xxx')
    print('yyy')

print()

with manager():
    print('Python')
    print(4 + 15 / 3)
    print('Runtime')
    print('Context')
