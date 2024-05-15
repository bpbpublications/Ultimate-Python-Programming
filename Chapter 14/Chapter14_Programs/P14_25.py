class Account():
    rate = 5

a1 = Account()
a2 = Account()

print(Account.rate, a1.rate, a2.rate)
Account.rate = 6
print(Account.rate, a1.rate, a2.rate)
a1.rate = 7
print(Account.rate, a1.rate, a2.rate)

print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)


