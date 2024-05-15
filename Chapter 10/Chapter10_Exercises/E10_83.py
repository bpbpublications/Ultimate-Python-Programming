def median(*args):
    numbers = sorted(args)
    mid = len(numbers) // 2
    if len(numbers) % 2 != 0:
        return numbers[mid]
    return (numbers[mid - 1] + numbers[mid]) / 2


print(median(5, 3, 4, 5, 6, 5, 7, 8, 6))
print(median(5, 4, 3, 7, 5, 6))
nums = [2, 4, 5, 8, 6, 6, 3, 9]
print(median(*nums))
