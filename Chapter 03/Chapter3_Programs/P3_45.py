import unicodedata

s = 'नमस्ते Hello 🙏'
for i in range(len(s)):
    print(unicodedata.name(s[i]))
