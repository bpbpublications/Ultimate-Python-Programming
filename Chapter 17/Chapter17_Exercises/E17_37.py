def generate_multiples(number, n):
    for i in range(n):
        yield number * (i + 1)

for i in generate_multiples(6, 10):
    print(i, end=' ')

