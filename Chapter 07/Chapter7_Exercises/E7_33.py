age = input('Enter your age : ')
while not age.isnumeric() or int(age) > 100 or int(age) < 10:
    age = input('Wrong input\nEnter your age : ')
age = int(age)
print(age)
