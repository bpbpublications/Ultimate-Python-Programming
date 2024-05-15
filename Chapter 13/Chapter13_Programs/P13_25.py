with open('myfile.bin', 'wb') as f:
    data = '☛ Explicit is better than implicit ✍'
    f.write(data.encode('utf-8'))

with open('myfile.bin', 'rb') as f:
    s = f.read()
    data = s.decode('utf-8')
    print(data)
