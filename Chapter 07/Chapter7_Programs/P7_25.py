a = int(input("Enter first digit : "))
b = int(input("Enter second digit : "))
c = int(input("Enter third digit : "))
digits = [a, b, c]
numbers = []
for i in digits:
    for j in digits:
        for k in digits:
            numbers.append(i * 100 + j * 10 + k)
print(numbers)


numbers = []
for i in digits:
    for j in digits:
        for k in digits:
            if i != j and j != k and k != i:
                numbers.append(i * 100 + j * 10 + k)
print(numbers)

