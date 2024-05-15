L = ['a', 'b', 'c', 'd', 'e']
i1 = iter(L)
print(i1)
print(iter(i1))
print(i1 is iter(i1))
