from contextlib import contextmanager

@contextmanager
def manager():
    print('Entering')
    x = 5
    try:
       yield x
    finally:
       print('Exiting')

with manager():
    print('Python')
    print(4 + 15 / 0)
    print('Runtime')
    print('Context')
