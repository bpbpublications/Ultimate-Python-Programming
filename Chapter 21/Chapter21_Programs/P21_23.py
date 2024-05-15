# open a file only for reading

from contextlib import contextmanager

@contextmanager
def open_readonly(filename):
    file = open(filename, 'r')
    try:
        yield file
    finally:
        file.close()


with open_readonly('test.txt') as f:
    print(f.read())
