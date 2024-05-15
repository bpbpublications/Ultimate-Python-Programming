d1 = {num: [n for n in range(1, num + 1) if num % n == 0] for num in range(1, 20)}
print(d1)

d = {}
for num in range(1, 20):
    factors = [n for n in range(1, num + 1) if num % n == 0]
    d[num] = factors
print(d)
