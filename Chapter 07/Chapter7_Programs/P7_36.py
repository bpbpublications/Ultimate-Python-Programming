fruit_prices = {'apple': 210, 'banana': 100, 'grapes': 90}

done = False
while not done:
    fruit = input('Enter fruit name : ')
    price = int(input('Enter price : '))

    if price > 200:
        print('Price more than 200 not allowed')
    else:
        print('Do something')
        print('Do something')
        fruit = fruit.lower()
        if price < 30:
            price += 10
        fruit_prices[fruit] = price
        if input('Want to enter more(y/n) : ') == 'n':
            done = True
print(fruit_prices)
