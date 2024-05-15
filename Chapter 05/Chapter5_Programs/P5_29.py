s1 = 'Welcome'
s2 = 'Come here'
print(set(s1) - set(s2))

s3 = 'What is in a name'
s4 = 'There are letters in a name'
print(set(s3.split()) - set(s4.split()))

x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]
print(set(x) | set(y))
