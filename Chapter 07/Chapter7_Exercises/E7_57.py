n = int(input('Enter a number : '))

i = 2
while n % i != 0:
    i += 1
print('Smallest divisor is:', i)

for i in range(2, n + 1):
    if n % i == 0:
        break
print('Smallest divisor is:', i)
