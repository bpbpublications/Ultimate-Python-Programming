currency = {}
currency['India'] = 'Rupee'
currency['UK'] = 'Pound'
currency['Japan'] = 'Yen'
currency['Austria'] = 'Euro'
currency['Bangladesh'] = 'Taka'

print(currency)
del currency['UK']
print(currency)

c = currency.pop('Japan')
print(currency)
print(c)

currency['Switzerland'] = 'Swiss Franc'
currency['India'] = 'Indian Rupee'
print(currency)

currency.popitem()
print(currency)

print(list(currency.keys()))
print(list(currency.values()))
print(list(currency.items()))
