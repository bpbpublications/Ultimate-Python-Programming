L = [1, 2, 3]
X = ['a', L]
X[1][0] = 100
print(L)

L = [1, 2, 3]
X = ['a', L[:]]
X[1][0] = 100
print(L)

L = [1, 2, 3]
X = ['a', L.copy()]
X[1][0] = 100
print(L)

L = [1, 2, 3]
X = ['a', list(L)]
X[1][0] = 100
print(L)
