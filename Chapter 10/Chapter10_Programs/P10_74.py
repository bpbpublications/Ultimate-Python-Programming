def func(s: str, i: 'int 0 to 5' = 0, j: int = 3) -> str:
    return s[i:j]


print(func.__annotations__)
help(func)

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 8))
