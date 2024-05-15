def reverse(sequence):
    for i in range(len(sequence) - 1, -1, -1):
        yield sequence[i]


for value in reverse([1, 2, 3, 4]):
    print(value)
