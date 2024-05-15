height = float(input('Enter your height in cms : '))
weight = float(input('Enter your weight in kgs : '))

height *= 0.01  # changing to meters

bmi = weight / (height * height)

print('Your Body Mass Index is - ', bmi)

if bmi < 18.5:
    print('You are underweight')
elif bmi <= 24.9:
    print('You have normal weight')
elif bmi <= 29.9:
    print('You are overweight')
else:
    print('You are obese')
