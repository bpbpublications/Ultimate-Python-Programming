def input_int(prompt='Enter an integer : '):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('The text you entered is not a valid integer')


n = input_int()
print(n + 100)
age = input_int('Enter age : ')
print(age)
