s1 = int(input('Enter first side : '))
s2 = int(input('Enter second side : '))
s3 = int(input('Enter third side : '))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Perimeter of the triangle is ', s1 + s2 + s3)
    if s1 == s2 == s3:
        print('Equilateral Triangle')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')
else:
    print('No triangle possible with these sides')
