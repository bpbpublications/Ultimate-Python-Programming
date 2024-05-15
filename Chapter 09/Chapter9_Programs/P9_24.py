text = "Hello World !!!"
d = {ch: text.count(ch) for ch in text}
print(d)

d = {ch: text.count(ch) for ch in set(text)}
print(d)

