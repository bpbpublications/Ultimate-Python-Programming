class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def __str__(self):
        return f'{self.nr}/{self.dr}'

    def __int__(self):
        return self.nr // self.dr

    def __float__(self):
        return self.nr / self.dr

    def __bool__(self):
        return True if self.nr != 0 else False

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return

        self.nr //= h
        self.dr //= h

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


f1 = Fraction(19, 2)
print(int(f1), float(f1), bool(f1))
f2 = Fraction(0, 3)
print(int(f2), float(f2), bool(f2))
