def list_to_csv(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        result = [str(value) for value in result]
        return ','.join(result)

    return wrapper


@list_to_csv
def func1():
    return [1, 2, 6.8, 9.8]


x = func1()
print(x)


def csv_to_list(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result.split(',')

    return wrapper


@csv_to_list
def func2():
    return 'John, 28, Delhi, 5000'


y = func2()
print(y)
