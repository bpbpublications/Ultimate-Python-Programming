M = [[1, 6, 2, 3],
     [7, 5, 6, 9],
     [8, 9, 3, 2]
     ]

T = [list(t) for t in zip(*M)]
print(T)
