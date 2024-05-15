L1 = list(filter(lambda x: x % 10 in (3, 6, 9), range(1, 101)))
print(L1)

L2 = [x for x in range(1, 101) if x % 10 in (3, 6, 9)]
print(L2)
