from time import time


class Timer():

    def __enter__(self):
        print('Starting timer')
        self.start = time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time()
        print('Timer stopped')
        time_taken = self.end - self.start
        print('Time taken is', time_taken)


print('Welcome')

with Timer():
    x = 999999
    y = x ** 566999

numbers = [1, 2, 3, 4]
print(numbers)

with Timer():
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
