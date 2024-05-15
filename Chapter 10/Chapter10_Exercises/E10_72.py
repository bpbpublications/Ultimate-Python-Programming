def find(data, value):
    for item in data:
        if item == value:
            return True
    return False


L = [2, 3, 4, 7, 8, 1]
T = (3, 5, 1, 7, 8)
S = 'Hello'
D = {1: 'a', 2: 'b', 3: 'c'}

print(find(L, 3))
print(find(L, 10))
print(find(T, 3))
print(find(T, 10))
print(find(S, 'e'))
print(find(S, 'x'))
print(find(D, 1))
print(find(D, 'a'))
