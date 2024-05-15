
numbers = [10, 2, 3, 41, 5, 7, 8, 9, 62]
evens = odds = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(evens)
print(odds)


numbers = [10, 2, 3, 41, 5, 7, 8, 9, 62]
evens = []
odds = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(evens)
print(odds)