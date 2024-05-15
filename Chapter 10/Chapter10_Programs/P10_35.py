def simple_interest(principal, time=2, rate=5):
    return (principal * rate * time) / 100


s1 = simple_interest(1000, 4, 7)
s2 = simple_interest(1000, 4)
s3 = simple_interest(1000)

print(s1, s2, s3)