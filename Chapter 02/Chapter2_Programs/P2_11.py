principal = float(input('Enter the principal : '))
time = int(input('Enter the time in years : '))
rate = float(input('Enter the interest rate : '))

simple_interest = (principal * time * rate) / 100
print('Simple interest is ', simple_interest)

compound_interest = principal * (1 + rate / 100) ** time - principal
print('Compound interest is ', compound_interest)
