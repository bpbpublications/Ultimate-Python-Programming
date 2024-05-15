def median1(numbers):
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 != 0:
        return numbers[mid]
    return (numbers[mid - 1] + numbers[mid]) / 2


def median2(numbers):
    numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 != 0:
        return numbers[mid]
    return (numbers[mid - 1] + numbers[mid]) / 2


nums1 = [2, 4, 5, 8, 6, 6, 3, 9]
nums2 = [2, 4, 5, 8, 6, 6, 3, 9]

print(median1(nums1), end='  ')
#print(median1(nums1[:]), end='  ')
print(median2(nums2), end='  ')

print(nums1, end='  ')
print(nums2)
