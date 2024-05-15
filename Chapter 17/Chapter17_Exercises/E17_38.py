def gen_factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


for i in gen_factors(500):
    print(i, end=' ')
