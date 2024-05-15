total = 0
while True:
    n = int(input('Enter a number : '))
    if n == 0:
        break
    if n < 0 or n > 500:
        print('Not adding this number')
        continue
    total += n
print(total)
