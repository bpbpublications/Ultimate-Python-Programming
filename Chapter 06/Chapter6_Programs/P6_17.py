ch = input('Enter a single character : ')
if len(ch) != 1:
    print('You did not enter a single character')
elif ch.isupper():
    print('Uppercase letter')
elif ch.islower():
    print('Lowercase letter')
elif ch.isnumeric():
    print('Number')
elif ch.isspace():
    print('Space')
else:
    print('Special character')
print('Bye')
