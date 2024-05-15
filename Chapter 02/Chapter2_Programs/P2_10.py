length = float(input('Enter length of rectangle in cm : '))
breadth = float(input('Enter breadth of rectangle in cm : '))

area = length * breadth
perimeter = 2 * (length + breadth)
diagonal = (length*length + breadth*breadth) ** 0.5

print('Area of rectangle is ', area, 'sq cm')
print('Perimeter of rectangle is ', perimeter, 'cm')
print('Diagonal of rectangle is ', diagonal, 'cm')
