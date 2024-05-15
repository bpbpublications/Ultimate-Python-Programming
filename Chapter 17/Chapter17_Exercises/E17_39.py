def gen_factor_pairs(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            yield i, n // i
        i += 1


for i in gen_factor_pairs(500):
    print(i, end=' ')

print()
g = gen_factor_pairs(10)
print(next(g), next(g))
