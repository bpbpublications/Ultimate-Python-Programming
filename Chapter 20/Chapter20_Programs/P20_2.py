marks = [34, 32, 45]
for i in range(4):  # IndexError: list index out of range
    print(marks[i])
print(mark[0])  # NameError: name 'mark' is not defined

marks.popitem(2)  # AttributeError: 'list' object has no attribute 'popitem'

x = marks[0] / (marks[1] - 32)  # ZeroDivisionError: division by zero

print(int('ten'))  # ValueError: invalid literal for int() with base 10: 'ten’

print(len(12345))  # TypeError: object of type 'int' has no len()

marks2 = marks + 2  # TypeError: can only concatenate list (not "int") to list

pow(2)  # TypeError: pow() missing required argument 'exp' (pos 2)
