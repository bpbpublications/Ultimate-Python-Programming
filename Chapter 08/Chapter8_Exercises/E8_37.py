from random import randint

secret = randint(1, 100)
print('The secret number is in between 0 and 100')
attempts = 0
while True:
    n = int(input('Enter a number : '))
    if n > secret:
        print('Bigger than the secret number')
    elif n < secret:
        print('Smaller than the secret number')
    else:
        print('You guessed it right')
        break
    attempts += 1
    if attempts == 10:
        print('No more attempts')
        print(f'Secret number is {secret}')
        break
