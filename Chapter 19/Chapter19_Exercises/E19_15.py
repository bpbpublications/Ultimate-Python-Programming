L = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
print(sorted(L, key=lambda t: len(t[1])))
