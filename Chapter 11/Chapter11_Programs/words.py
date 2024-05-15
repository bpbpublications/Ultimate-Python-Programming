

# count words
def count(string):
    return len(string.split(' '))


# first word
def first(string):
    return string.split(' ')[0]


# last word
def last(string):
    return string.split(' ')[-1]


# sorted words
def ordered(string):
    return ' '.join(sorted(string.split(' ')))


# return a string with each word reversed
def reverse(string):
    words = string.split(' ')
    return ' '.join([word[::-1] for word in words])
