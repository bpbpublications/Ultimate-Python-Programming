s = set()
print(s)

print(set('HELLO'))

L = [1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1]
print(set(L))

t = (20, 30, 40, 30, 20)
print(set(t))

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'd'}
print(set(d))

print(set(d.values()))

odds = set(range(1, 20, 2))
print(odds)
