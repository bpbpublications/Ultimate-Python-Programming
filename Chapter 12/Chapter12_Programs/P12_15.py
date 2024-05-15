x = 100

def func():
   x = 30
   print(x)
   print(locals())
   print(globals())

func()
print(x)
