L1 = [method for method in dir(str) if not method.startswith('_')]
L2 = [method for method in dir(str) if method.startswith('is')]
print(L1)
print(L2)