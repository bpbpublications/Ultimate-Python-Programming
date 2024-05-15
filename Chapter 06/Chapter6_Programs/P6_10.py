s = input('Enter a string : ')
if s == s[::-1]:
    if len(s) < 5:
        print(f'{s} is a small palindrome')
    else:
        print(f'{s} is a big palindrome')
else:
    print(f'{s} is not a palindrome')
