total = 0
while total <= 100:
    num = int(input('Enter a number : '))
    total += num
print(total)

total = 0
while total <= 100:
    num = int(input('Enter a number : '))
    if num < 0:
        break
    total += num
print(total)
