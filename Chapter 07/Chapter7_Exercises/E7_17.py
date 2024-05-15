n = 2345
sum = 0
while n > 0:
    rem = n % 10
    sum += rem
    n //= 10
print(sum)
