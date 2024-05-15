s1 = input('Enter first phrase : ')
s2 = input('Enter second phrase : ')

s1 = s1.replace(' ', '').lower()
s2 = s2.replace(' ', '').lower()

if len(s1) == len(s2) and set(s1) == set(s2):
    print('Strings are anagrams')
else:
    print('Strings are not anagrams')
