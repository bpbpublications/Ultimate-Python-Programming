print('AS😄'.encode('utf-8'))  # bytes representation of string according to utf-8 encoding

print(b'AS\xf0\x9f\x98\x84'.decode('utf-8'))  # converting encoded bytes back to Unicode string

print('AS😄'.encode('utf-32'))

print(b'\xff\xfe\x00\x00A\x00\x00\x00S\x00\x00\x00\x04\xf6\x01\x00'.decode('utf-32'))

