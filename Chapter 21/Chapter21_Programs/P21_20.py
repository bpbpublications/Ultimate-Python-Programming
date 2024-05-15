from contextlib import contextmanager

@contextmanager
def manager():
    print('Entering')
    yield
    print('Exiting')

with manager():
    print('Python')
    print(4 + 15 / 0)
    print('Runtime')
    print('Context')

