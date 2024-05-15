import decimal

print(decimal.Decimal('22') / decimal.Decimal('7'))

with decimal.localcontext() as ctx:
    ctx.prec = 40
    print(decimal.Decimal('22') / decimal.Decimal('7'))

print(decimal.Decimal('22') / decimal.Decimal('7'))

with decimal.localcontext() as ctx:
    ctx.prec = 4
    print(decimal.Decimal('22') / decimal.Decimal('7'))
