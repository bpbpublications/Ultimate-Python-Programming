factorial = {0: 1}
for i in range(1, 8):
    factorial[i] = i * factorial[i - 1]
print(factorial)
