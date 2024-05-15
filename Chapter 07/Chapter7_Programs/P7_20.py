i = 1
while i <= 3:
    print('Outer while loop iteration', i)
    for j in range(1, 5):
        print('\tInner for loop iteration', j)
    i += 1
