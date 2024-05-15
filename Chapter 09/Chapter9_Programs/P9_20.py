matrix = [[1, 4, 8, 3],
          [2, 5, 6, 3],
          [7, 9, 5, 8],
          ]
L1 = [element * 2 for row in matrix for element in row]
print(L1)

L2 = [[element * 2 for element in row] for row in matrix]
print(L2)
