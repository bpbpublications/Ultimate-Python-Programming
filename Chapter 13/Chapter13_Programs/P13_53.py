import pickle

numbers = [10, 20, 30]
s = pickle.dumps(numbers)
print(type(s))

x = pickle.loads(s)
print(type(x))
print(x)
