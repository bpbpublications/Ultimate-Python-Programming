numbers = [82, 31, 55, 12, 7, 56, 99, 12, 99, 67, 12]
print(31 in numbers)
print(31 not in numbers)
print(100 not in numbers)

print(numbers.index(12))
print(numbers.index(12, 4))
print(numbers.index(12, 4, 10))
# print(numbers.index(100))
print(numbers.count(12))