from time import time
from contextlib import contextmanager

@contextmanager
def timer():
    print('Starting timer')
    start = time()
    yield
    end = time()
    print('Timer stopped')
    time_taken = end - start
    print('Time taken is', time_taken)

print('Welcome')

with timer():
    x = 999999
    y = x ** 566999

numbers = [1, 2, 3, 4]
print(numbers)

with timer():
    n = 141111
    fact = 1
    while n > 0:
        fact *= n
        n -= 1

with timer():
    x = 999999
    y = 674444
    z = x + 10000 ** y
print('Bye')
