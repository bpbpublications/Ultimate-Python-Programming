def fibo_gen(max):
    a = 0
    b = 1
    while a < max:
        yield a
        a, b = b, a + b


fib = fibo_gen(100)

for i in fib:
    print(i, end=' ')
