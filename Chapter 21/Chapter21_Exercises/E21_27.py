import contextlib
import sys

@contextlib.contextmanager
def repeater():
    originalwrite = sys.stdout.write

    def repeat(s):
        originalwrite(s * 2)

    sys.stdout.write = repeat
    try:
        yield
    finally:
        sys.stdout.write = originalwrite

print('Yes ', 'No', 1, 2)
print(2 + 3)
L = [1, 2, 3]
print(L)

with repeater():
    print('Yes ', 'No', 1, 2)
    print(2 + 3)
    L = [1, 2, 3]
    print(L)

print('Yes ', 'No', 1, 2)
