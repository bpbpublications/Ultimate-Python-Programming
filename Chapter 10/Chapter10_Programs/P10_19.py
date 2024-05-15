def func(text):
    up = low = dig = 0
    for ch in text:
        if ch.isupper():
            up += 1
        elif ch.islower():
            low += 1
        elif ch.isdigit():
            dig += 1
    return up, low, dig


uppers, lowers, digits = func('Fall down 7 times, Stand up 8')
print(f'Uppercase : {uppers}, Lowercase : {lowers}, Digits : {digits}')
t = func('Fall down 7 times, Stand up 8')
print(t)
