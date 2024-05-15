try:
    print(3 / 0)
except Exception:
    print('xx')
except ZeroDivisionError:
    print('yy')
