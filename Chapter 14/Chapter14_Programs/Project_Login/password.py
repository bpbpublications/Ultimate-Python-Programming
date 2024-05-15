from user import User
import pickle

print('1. Sign up')
print('2. Login')
print('3. Forgot password')

with open('users.pck', 'rb') as file:
    users = pickle.load(file)

usernames = [user.username for user in users]

response = int(input('Enter your choice : '))

if response == 1:  # signup
    name = input('Enter a username for your account : ')
    while name in usernames:
        name = input('This username already present, enter another name : ')
    new_user = User(name)
    new_user.sign_up()
    users.append(new_user)
else:  # login or forgot password
    name = input('Enter your username : ')
    while name not in usernames:
        print('Invalid Username')
        name = input('Enter a valid username : ')

    for user in users:
        if user.username == name:
            if response == 2:
                user.log_in()
            else:
                user.forgot_password()

with open('users.pck', 'wb') as file:
    pickle.dump(users, file)
