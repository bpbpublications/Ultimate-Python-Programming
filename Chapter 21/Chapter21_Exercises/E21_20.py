import sys


class Repeater:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.repeat

    def repeat(self, s):
        self.original_write(s * 2)

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write


print('Yes ', 'No', 1, 2)
print(2 + 3)
L = [1, 2, 3]
print(L)

with Repeater():
    print('Yes ', 'No', 1, 2)
    print(2 + 3)
    L = [1, 2, 3]
    print(L)

print('Yes ', 'No', 1, 2)
