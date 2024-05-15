s1 = input('Enter first string : ')
s2 = input('Enter second string : ')
L = list(set(s1) & set(s2))
print(L)

string1 = 'Life has no remote, get up and change it yourself'
string2 = 'Life has no ctrl+Z'
s = set(string1.split(' ')) & set(string2.split(' '))
print(s)