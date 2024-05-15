from contextlib import contextmanager

@contextmanager

def manager():
    print('Entering', end =' ')
    v = 100
    yield v
    print('Exiting')
    
with manager() as var:
    print(var, end =' ')
