def str_lower_int_abs(fn):
    def wrapper(*args, **kwargs):
        new_args = []
        for value in args:
            if isinstance(value, str):
                new_args.append(value.lower())
            elif isinstance(value, int):
                new_args.append(abs(value))
            else:
                new_args.append(value)

        for key, value in kwargs.items():
            if isinstance(value, str):
                kwargs[key] = value.lower()
            elif isinstance(value, int):
                kwargs[key] = abs(value)

        return fn(*new_args, **kwargs)

    return wrapper


@str_lower_int_abs
def func1(a, b, c, d):
    print(a, b, c, d)


func1(2, 'RR', c=-6, d='Xyz')

