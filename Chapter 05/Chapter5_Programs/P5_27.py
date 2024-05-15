s1 = {1, 2, 4, 3, 6}
s2 = {6, 4, 3, 2, 1}
print(s1 == s2)

s1 = {'x', 'y', 'z', 'a', 'b'}
s2 = {'x', 'y', 'z', 'a', 'b', 'c', 'd'}
s3 = {'a', 'b', 'x', 'y', 'z'}

print(s1.issubset(s2))
print(s1 <= s2)
print(s2.issuperset(s1))
print(s2 >= s1)
print(s1 <= s3)
print(s1 >= (s3))
print(s1 <= s1)
print(s1 >= s1)
print(s1 < s2)
print(s1 < s3)
print(s3 > s1)
