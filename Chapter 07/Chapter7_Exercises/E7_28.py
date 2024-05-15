text = 'Humpty Dumpty sat on a wall Humpty Dumpty had a great fall '
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
print(count)

import string

text = 'Humpty, Dumpty sat on a wall. Humpty2, #Dumpty2 had a great fall 333 !!!'
words = {}
for word in text.lower().split():
    word = word.strip(string.digits + string.punctuation + string.whitespace)
    if word:
        words[word] = words.get(word, 0) + 1
print(words)

# The string module in Python provides a collection of string constants, including letters, digits,
# and various punctuation characters.
# We can use these constants for various string-related operations as we have done in this program.
