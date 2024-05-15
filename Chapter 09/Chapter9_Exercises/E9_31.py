M1 = [[1, 4, 8, 3],
      [2, 5, 6, 3],
      [7, 9, 5, 8]
      ]
M2 = [[3, 5, 2, 3],
      [5, 2, 7, 9],
      [2, 8, 1, 8]
      ]

M3 = [[M1[row][col] + M2[row][col] for col in range(4)] for row in range(3)]
print(M3)
M3 = [[x1 + x2 for x1, x2 in zip(m1, m2)] for m1, m2 in zip(M1, M2)]
print(M3)
