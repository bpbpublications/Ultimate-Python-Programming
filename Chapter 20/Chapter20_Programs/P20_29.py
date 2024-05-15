try:
    age = int(input('Enter age : '))
    if age < 0 or age > 120:
      raise ValueError('Age not in valid range')
except ValueError as e:
    print('Invalid value for age')
    print(e)
else:
    print('Age is', age)
