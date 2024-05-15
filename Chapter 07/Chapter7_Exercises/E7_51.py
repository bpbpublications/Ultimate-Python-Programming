import random

while True:
    print('Rolling the dice')
    print(random.randint(1, 6))
    response = input('Want to roll again(y/n) ? ')
    if response != 'y':
        break
