def func(symbol):
    return lambda message: print(message + symbol)


exclaim = func('!!!!!')
question = func('???')
sentence = func('.')

exclaim('OMG')
question('What is this')
sentence('Python is easy')
exclaim('Really')
