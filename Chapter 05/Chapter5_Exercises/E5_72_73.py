matrix = {(0, 5): 4, (1, 3): 8, (3, 4): 6, (5, 2): 3}

print(matrix[0, 5])

print(matrix.get((1, 3), 0))
print(matrix.get((1, 2), 0))
