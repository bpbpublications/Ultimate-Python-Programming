f = open('testfile.bin', 'w+b')
f.write(b'abcdefghijklmn')
f.write(b'123456789')
print(f.tell())
print(f.read())
f.seek(0)
print(f.read())
print(f.tell())
f.seek(-9, 2)
print(f.read(3))
print(f.tell())
f.seek(0, 2)
print(f.tell())
f.close()
