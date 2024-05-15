from time import time

class Timer():
    def __init__(self, warn_seconds=10):
        self.warn_seconds = warn_seconds

    def __enter__(self):
        print('Starting timer')
        self.start = time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time()
        print('Timer stopped')
        time_taken = self.end - self.start
        print('Time taken is', time_taken)
        if time_taken > self.warn_seconds:
            print('Took very long ............. ')


print('Welcome')

with Timer(4):
    x = 999999
    y = x ** 566999

numbers = [1, 2, 3, 4]
print(numbers)

with Timer(3):
    n = 141111
    fact = 1

    while n > 0:
        fact *= n
        n -= 1

with Timer():
    x = 999999
    y = 674444
    z = x + 10000 ** y

print('Bye')
