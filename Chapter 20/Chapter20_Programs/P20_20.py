try:
    import test
except SyntaxError as e:
    print(e.args)
    for attr in dir(e):
        if not attr.startswith("_"):
               print(attr, "=", e.__getattribute__(attr))
