def convert(num, base):
    symbols = '0123456789ABCDEF'
    if num < base:
        return symbols[num]
    else:
        return convert(num // base, base) + symbols[num % base]


print(convert(6341, 2))
print(convert(6341, 8))
print(convert(6341, 16))
