import sys
from contextlib import contextmanager


@contextmanager
def output_manager(filename):
    print('Redirecting Output to', filename, '.....')
    f = open(filename, 'a')
    original = sys.stdout
    sys.stdout = f
    try:
        yield
    finally:
        sys.stdout = original
        f.close()
        print('Output prints to screen now.....')


print('Welcome')

numbers = [1, 2, 3, 4]
print(numbers)
print(numbers * 2)

with output_manager('test.txt'):
    for n in numbers:
        print(sum(range(1, n + 1)), end=' ')
    print()
    print([x * 100 for x in numbers])

d = {61: 'a', 32: 'b', 31: 'c'}
print(d)
print(sorted(d.keys()))

with output_manager('log.txt'):
    s1 = {'x', 'a', 'b'}
    s2 = {'x', 'a', 'b', 'c', 'd'}
    print(s1 | s2)
    print(s2 - s1)

print(2 + 3 * 5)
print('Bye')
