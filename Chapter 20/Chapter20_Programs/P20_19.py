try:
    import test
except SyntaxError as e:
    print(e.args)
