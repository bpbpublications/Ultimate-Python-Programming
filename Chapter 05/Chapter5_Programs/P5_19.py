shop1_prices = {'apple': 200,
                'mango': 250,
                'banana': 100,
                'grapes': 90
                }

shop2_prices = shop1_prices.copy()

print(shop2_prices)
shop2_prices['apple'] -= 40
shop2_prices['banana'] -= 20
print(shop2_prices)

bill = 2 * shop1_prices['apple'] + 3 * shop1_prices['banana']
print(bill)

print(shop1_prices)