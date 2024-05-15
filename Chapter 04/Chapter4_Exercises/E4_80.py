numbers = [12, 32, 55, 67, 3, 55, 68, 22, 55, 89, 55, 1, 19, 32]
print(len(numbers) - numbers[::-1].index(55) - 1)
