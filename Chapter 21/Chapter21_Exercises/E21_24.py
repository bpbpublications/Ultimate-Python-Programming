from contextlib import contextmanager
from time import time


@contextmanager
def timed_open(filename, mode):
    f = open(filename, mode)
    try:
        print('Starting timer')
        start = time()
        yield f
        end = time()
        print('Timer stopped')
        time_taken = end - start
        print('Time taken is', time_taken)
    finally:
        f.close()


with timed_open('test.txt', 'r') as f:
    print(f.read())
