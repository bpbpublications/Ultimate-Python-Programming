import random


class User:

    def __init__(self, username):
        self.username = username
        self.password = ''
        self.phone = ''
        self.security_questions = {}
        self.blocked = False

    def sign_up(self):
        self.password = self._enter_password()
        self.phone = input('Enter your phone number : ')
        print('Answer these two security questions')
        print('These questions will help you login if you forget your password ')

        with open('questions.txt', 'r') as file:
            questions = file.readlines()

        random.shuffle(questions)
        answer0 = input(questions[0])
        answer1 = input(questions[1])

        self.security_questions[questions[0]] = answer0
        self.security_questions[questions[1]] = answer1

    def log_in(self):
        if self.blocked == True:
            print('This account is blocked')
            return

        psswd_attempts = 1
        password = input('Enter password : ')
        while password != self.password:
            if psswd_attempts == 3:
                self.blocked = True
                print('Sorry, no more tries !\n')
                break
            print('Wrong Password')
            password = input('Enter correct password : ')
            psswd_attempts += 1
        else:
            print(f'Welcome,{self.username}')

    def forgot_password(self):
        if self.blocked == True:
            print('This account is blocked')
            return

        for question, answer in self.security_questions.items():
            response = input(question)
            if response != answer:
                print('You answered it wrong')
                print('Sending an OTP to your phone ending with ', self.phone[-5:])
                self._send_and_check_otp()
                break
        else:
            print('Your password is ', self.password)
            self.log_in()

    def _send_and_check_otp(self):
        otp = random.randint(100000, 999999)
        print(otp)
        n = int(input('Enter the otp sent on your phone '))
        if n == otp:
            print('Your password is ', self.password)
            self.log_in()
        else:
            print('Wrong OTP')

    def _enter_password(self):
        while True:
            password = input('Enter password : ')
            if len(password) < 7:
                print('Password should have at least 7 characters')
                continue
            a = d = w = 0
            for ch in password:
                if ch.isalpha():
                    a += 1
                elif ch.isdigit():
                    d += 1
                elif ch.isspace():
                    w += 1
            if a < 2:
                print('Password should have at least 2 letters')
                continue
            if d == 0:
                print('Password should have at least one digit')
                continue
            if w > 0:
                print('Whitespace not allowed')
                continue

            if len(password) < 12:
                print('Weak password ')
                response = input('Do you want to enter another password : (yes/no)')
                if response == 'yes':
                    continue
                else:
                    break
            else:
                print('Strong password ')
                break

        return password
