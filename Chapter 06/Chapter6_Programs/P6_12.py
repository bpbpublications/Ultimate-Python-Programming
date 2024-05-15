marks = int(input('Enter marks : '))
if marks >= 70:
    print('Well done, you have got A grade')
    if marks >= 90:
        print('You are awarded a scholarship')
else:
    print('Try to get A grade next time')
    if marks < 40:
        print('You really need to work hard')
