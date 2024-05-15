data = '±µ'
binary_data = data.encode('utf-8')
print(binary_data.decode('latin-1'))


data = 'εθ'
binary_data = data.encode('utf-8')
print(binary_data.decode('utf-16'))


data = 'AS😄'
binary_data = data.encode('utf-32')
print(binary_data.decode('utf-8'))  # will give UnicodeDecodeError
