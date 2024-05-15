fruit_prices = {'apple': 210, 'banana': 100, 'grapes': 90}
done = False
while not done:
    fruit = input('Enter fruit name : ')
    price = int(input('Enter price : '))
    fruit_prices[fruit] = price
    if input('Want to enter more(y/n) : ') == 'n':
        done = True
print(fruit_prices)

fruit_prices = {'apple': 210, 'banana': 100, 'grapes': 90}
while True:
    fruit = input('Enter fruit name : ')
    price = int(input('Enter price : '))
    fruit_prices[fruit] = price
    if input('Want to enter more(y/n) : ') == 'n':
        break
print(fruit_prices)
