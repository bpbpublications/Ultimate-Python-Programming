def func():
    raise ZeroDivisionError


try:
    func()
except (TypeError, ValueError):
    pass
except:
    raise
