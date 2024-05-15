import string

with open('data2.txt', 'r') as f:
    words = {}
    for line in f:
        for word in line.lower().split():
            word = word.strip(string.digits + string.punctuation )
            if word:
                words[word] = words.get(word, 0) + 1
    print(words)



