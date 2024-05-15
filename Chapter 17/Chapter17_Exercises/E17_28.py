def enumerate1(sequence, start=0):
    n = start
    for element in sequence:
        yield n, element
        n += 1


L = [10, 20, 30]
t = (8, 9, 10, 11, 12)

for i, value in enumerate1(L):
    print(i, value)

for i, value in enumerate1(t, 2):
    print(i, value)
