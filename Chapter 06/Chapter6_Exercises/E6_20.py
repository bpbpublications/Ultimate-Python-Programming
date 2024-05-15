bill_amount = 300
if bill_amount > 2000:
    free_home_delivery = 'Available'
else:
    free_home_delivery = 'Not Available'
print(free_home_delivery)

free_home_delivery = 'Available' if bill_amount > 2000 else 'Not Available'
print(free_home_delivery)
