from contextlib import contextmanager
@contextmanager
def manager():
    print('Entering', end =' ')
    yield
    print('Exiting')

with manager() as var:
    print(var, end =' ')
