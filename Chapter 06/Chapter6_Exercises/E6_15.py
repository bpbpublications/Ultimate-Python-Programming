option1 = input('Enter your choice of unit for height(c for cm, i for inch) : ')
height = float(input('Enter your height : '))

if option1 == 'c':
    height *= 0.01
else:
    height *= 0.0254

option2 = input('Enter your choice of unit for weight(k for kg, p for pound) : ')
weight = float(input('Enter your weight : '))

if option2 == 'p':
    weight *= 0.4535924

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
