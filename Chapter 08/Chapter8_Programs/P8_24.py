total = 0
number = 0
while number != -1:
    number = int(input('Enter a number(-1 to quit) : '))
    total += number
print(total)

total = 0
while True:
    number = int(input('Enter a number(-1 to quit) : '))
    if number == -1:
        break
    total += number
print(total)
