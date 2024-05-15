def compound_interest(principal, time, rate=5):
    amount = principal * pow((1 + rate / 100), time)
    return amount - principal


print(compound_interest(1000, 3))
print(compound_interest(1000, 3, 6))
