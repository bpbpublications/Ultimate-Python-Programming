numbers = [2, 3, -7, 8, -5, -2, 9, 10]
for number in numbers:
    if number < 0:
        numbers.remove(number)
print(numbers)

numbers = [2, 3, -7, 8, -5, -2, 9, 10]
for number in numbers:
    print(number, end=' ')
    if number < 0:
        numbers.remove(number)
print(numbers)

numbers = [2, 3, -7, 8, -5, -2, 9, 10]
for number in numbers[:]:
    if number < 0:
        numbers.remove(number)
print(numbers)
