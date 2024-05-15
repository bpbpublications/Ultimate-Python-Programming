class OpenReadOnly:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename, 'r')
        return self.f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()


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


with OpenReadOnly('test.txt') as file, Timer():
    print(file.read(), end='')
