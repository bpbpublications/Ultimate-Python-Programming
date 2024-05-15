def fibo_gen(max):
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibo_gen(100)

for i in fib:
    if i > 500:
        break
    print(i, end=' ')
