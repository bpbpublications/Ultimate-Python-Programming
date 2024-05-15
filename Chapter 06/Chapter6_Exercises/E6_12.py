s = input('Enter a string : ')

if s.replace(' ', '').lower() == s[::-1].replace(' ', '').lower():
    print('String is a palindrome')
else:
    print('String is not a palindrome')
