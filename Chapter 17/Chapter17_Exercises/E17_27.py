def range1(start, stop=None, step=1):
    if stop is None:  # done this so that the calls such as range1(5) work
        stop = start
        start = 0
    while start < stop:
        yield start
        start += step


for x in range1(1, 5):
    print(x)

for x in range1(5):
    print(x)

for x in range1(1, 5, 0.5):
    print(x)
