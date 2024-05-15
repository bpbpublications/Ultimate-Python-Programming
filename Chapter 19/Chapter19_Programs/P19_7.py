L = ['elephant', 'bear', 'Duck', 'Fox', 'Giraffe']
print(sorted(L))

print(sorted(L, key=len))

print(sorted(L, key=str.lower))
print(sorted(L, key=str.upper))
print(sorted(L, key = lambda s : s.lower()[::-1]))