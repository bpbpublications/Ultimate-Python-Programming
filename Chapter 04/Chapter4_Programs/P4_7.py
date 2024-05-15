numbers = [10, 20, 30, 40, 50, 60, 70, 80]
numbers.clear()
print(numbers)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
del numbers[:]
print(numbers)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
numbers[:] = []
print(numbers)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(id(numbers))
numbers = []   #assigns a new empty list, not an in-place clearing
print(numbers)
print(id(numbers))