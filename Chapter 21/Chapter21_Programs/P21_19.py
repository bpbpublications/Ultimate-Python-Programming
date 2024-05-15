from contextlib import contextmanager


@contextmanager
def manager():
    print('Entering')
    x = 5
    yield x
    print('Exiting')


with manager() as var:
    print('xxx')
    print('yyy')
    print(var)

print()

with manager():
    print('Python')
    print(4 + 15 / 3)
    print('Runtime')
    print('Context')
