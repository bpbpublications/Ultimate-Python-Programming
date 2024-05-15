import sys

class OutputManager():

    def __enter__(self):
        print('Redirecting Output to test.txt.....')
        self.f = open('test.txt', 'a')
        self.original = sys.stdout
        sys.stdout = self.f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.original
        self.f.close()
        print('Output prints to screen now.....')


print('Welcome')

numbers = [1, 2, 3, 4]
print(numbers)
print(numbers * 2)

with OutputManager():
    for n in numbers:
        print(sum(range(1, n + 1)), end=' ')
    print()
    print([x * 100 for x in numbers])

d = {61: 'a', 32: 'b', 31: 'c'}
print(d)
print(sorted(d.keys()))

with OutputManager():
    s1 = {'x', 'a', 'b'}
    s2 = {'x', 'a', 'b', 'c', 'd'}
    print(s1 | s2)
    print(s2 - s1)

print(2 + 3 * 5)

print('Bye')
