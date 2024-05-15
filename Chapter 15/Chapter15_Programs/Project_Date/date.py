class Date:
    def __init__(self, d, m, y):
        self._d = d
        self._m = m
        self._y = y

        if not self._is_valid():
            raise ValueError('This date is not valid')

    @classmethod
    def from_str(cls, s):
        if len(s) != 10 or s[2] != '-' or s[5] != '-':
            raise ValueError('String not in correct format\nCorrect format is "dd-mm-yyyy"')
        d, m, y = s.split('-')
        return cls(int(d), int(m), int(y))

    @classmethod
    def from_date(cls, obj):
        return cls(obj._d, obj._m, obj._y)

    @classmethod
    def today(cls):
        from time import ctime
        s = ctime()  # This form 'Tue Jul 30 11:40:47 2019'
        s = s.replace('  ', ' ')  # if day is single digit, then we will get a double space
        _, m, d, _, y = s.split(' ')

        months = ('', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        return Date(int(d), months.index(m), int(y))

    # Read-only field accessors
    @property
    def year(self):
        return self._y

    @property
    def month(self):
        return self._m

    @property
    def day(self):
        return self._d

    def _is_valid(self):
        if self._y < 1500 or self._y > 2500:
            return False
        if self._m < 1 or self._m > 12:
            return False
        if self._d < 1 or self._d > _days_in_month(self._m, self._y):
            return False
        return True

    def add_years(self, iyear):
        d = self._d
        m = self._m
        y = self._y + iyear

        if d == 29 and m == 2 and not is_leap(y):
            d = 28
        return Date(d, m, y)

    def sub_years(self, dyear):
        d = self._d
        m = self._m
        y = self._y - dyear

        if d == 29 and m == 2 and not is_leap(y):
            d = 28
        return Date(d, m, y)

    def add_months(self, imonth):
        d = self._d
        m = self._m + (imonth % 12)
        y = self._y + (imonth // 12)

        if m > 12:
            m = m - 12
            y = y + 1

        dm = _days_in_month(m, y)
        if d > dm:
            d = dm

        return Date(d, m, y)

    def sub_months(self, dmonth):
        d = self._d
        m = self._m - (dmonth % 12)
        y = self._y - (dmonth // 12)

        if m <= 0:
            m = m + 12
            y = y - 1

        dm = _days_in_month(m, y)
        if d > dm:
            d = dm

        return Date(d, m, y)

    def add_days(self, days):
        j1 = self._julian()
        n = 366 - j1 if is_leap(self._y) else 365 - j1

        if days <= n:
            j2 = j1 + days
            y2 = self._y
        else:
            days -= n
            y2 = self._y + 1

            k = 366 if is_leap(y2) else 365

            while days >= k:
                if is_leap(y2):
                    days -= 366
                else:
                    days -= 365
                y2 += 1
                k = 366 if is_leap(y2) else 365
            j2 = days

        return _date_from_julian(j2, y2)

    def sub_days(self, days):
        j1 = self._julian()

        if days < j1:
            j2 = j1 - days
            y2 = self._y
        else:
            days = days - j1  # Now subtract days from 1st Jan y1
            y2 = self._y - 1

            k = 366 if is_leap(y2) else 365
            while days >= k:
                if is_leap(y2):
                    days -= 366
                else:
                    days -= 365
                y2 -= 1
                k = 366 if is_leap(y2) else 365

            j2 = 366 - days if is_leap(y2) else 365 - days

        return _date_from_julian(j2, y2)

    def __str__(self):
        return f'{self._d}/{self._m}/{self._y}'

    def __repr__(self):
        return f'Date({self._d}, {self._m}, {self._y})'

    def __eq__(self, other):
        return True if _cmp(self, other) == 0 else False

    def __lt__(self, other):
        return True if _cmp(self, other) == 1 else False

    def __le__(self, other):
        return True if (_cmp(self, other) == 0 or _cmp(self, other) == 1) else False

    def __add__(self, other):
        if isinstance(other, int):
            return self.add_days(other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Date):
            return self.diff_days(other)
        elif isinstance(other, int):
            return self.sub_days(other)
        else:
            return NotImplemented

    def _julian(self):
        j = self._d
        for i in range(1, self._m):
            j += _days_in_month(i, self._y)
        return j

    def diff_days(self, date2):
        if date2 > self:
            raise ValueError('Second date should fall before first date')
        j1 = self._julian()
        j2 = date2._julian()

        if self._y == date2._y:
            return j1 - j2

        d = 0
        for year in range(date2._y + 1, self._y):
            if is_leap(year):
                d += 366
            else:
                d += 365

        if is_leap(date2._y):
            return (366 - j2) + d + j1
        else:
            return (365 - j2) + d + j1

    def diff_ymd(self, date2):
        if date2 > self:
            raise ValueError('Second date should fall before first date')

        d1, m1, y1 = self._d, self._m, self._y
        d2, m2, y2 = date2._d, date2._m, date2._y

        if d1 < d2:
            if m1 != 1:
                d1 += _days_in_month(m1 - 1, y1)
                m1 = m1 - 1
            else:
                d1 += 31
                m1 = 12
                y1 = y1 - 1

        if m1 < m2:
            m1 = m1 + 12
            y1 = y1 - 1

        return y1 - y2, m1 - m2, d1 - d2

    def day_of_week(self):
        weekday_name = ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
        j = self._julian()
        f = (self._y - 1) // 4
        h = (self._y - 1) // 100
        fh = (self._y - 1) // 400

        d = (self._y + j + f - h + fh) % 7
        return weekday_name[d]

    def next_sunday(self):
        day = self.day_of_week()
        weekday_name = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
        i = weekday_name.index(day)
        return self.add_days(7 - i)

    def next_weekday(self):
        day = self.day_of_week()
        if day == 'Friday':
            return self.add_days(3)
        elif day == 'Saturday':
            return self.add_days(2)
        return self.add_days(1)


def _cmp(date1, date2):
    if date1._y < date2._y:
        return 1
    if date1._y > date2._y:
        return -1
    if date1._m < date2._m:
        return 1
    if date1._m > date2._m:
        return -1
    if date1._d < date2._d:
        return 1
    if date1._d > date2._d:
        return -1
    return 0


def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def _days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    if month == 2:
        if is_leap(year):
            return 29
        else:
            return 28


def _date_from_julian(j, year):
    for month in range(1, 13):
        dm = _days_in_month(month, year)
        if j <= dm:
            break
        j -= dm
    return Date(j, month, year)


if __name__ == '__main__':
    d1 = Date(2, 12, 1988)
    d2 = Date.from_str('01-11-1985')
    d3 = Date.today()
    d4 = Date.from_date(d1)
    print(d1.year, d1.month, d1.day)
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d1 - d2)
    print(d1 + 10)
    print(d2 - 10)
    print(d1.add_years(5))
    print(d2.sub_years(5))
    print(d1.add_months(15))
    print(d2.sub_months(15))
    print(d1.add_days(1000))
    print(d2.sub_days(1000))
    print(d1 < d2)
    print(d1.day_of_week())
    print(d1.next_sunday())
    print(d1.next_weekday())
    print(d1.diff_ymd(d2))
    print(d1.diff_days(d2))
