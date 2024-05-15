def input_value(value_type, prompt='Enter a value of type '):
    while True:
        try:
            if prompt == 'Enter a value of type ':
                prompt = prompt + str(value_type) + ' : '
            return value_type(input(prompt))
        except ValueError:
            print('The text you entered is not of type', str(value_type))


n = input_value(int)
print(n + 100)
age = input_value(int, 'Enter age : ')
print(age)

x = input_value(float)
print(x)
length = input_value(float, 'Enter length : ')
print(length)
