numbers = [10, 20, 30]
nums = [1, 2, 3, 4]
numbers.extend(nums)
print(numbers)

numbers = [10, 20, 30]
numbers.append(nums)
print(numbers)

numbers = [10, 20, 30]
numbers.extend('abcd')
print(numbers)

numbers += [98, 99, 100]
print(numbers)

