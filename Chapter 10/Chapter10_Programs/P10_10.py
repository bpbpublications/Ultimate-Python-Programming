def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si


principal = 2000
rate = 5
time = 4
interest = simple_interest(principal, rate, time)
amount = principal + interest
print(f'Simple interest is {interest}')
print(f'Amount is is {amount}')
