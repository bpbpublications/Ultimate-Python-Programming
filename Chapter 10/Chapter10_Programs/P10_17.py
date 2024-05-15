def is_valid(age):
    if not age.isdigit():
        return False
    age = int(age)
    if age <= 18 or age >= 75:
        return False
    return True


age = input('Enter age : ')
while not is_valid(age):
    age = input('Enter age : ')
print(f'Age is {age}')



