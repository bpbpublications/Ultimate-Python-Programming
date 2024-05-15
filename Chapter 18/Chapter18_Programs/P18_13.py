def trace(fn):
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} called')
        print(f'args : {args}  kwargs : {kwargs}')
        result = fn(*args, **kwargs)
        print(f'Return value : {result}\n')
        return result

    return wrapper


def capitalizer(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result.upper()

    return wrapper


@trace
@capitalizer
def username(email_id):
    return email_id[:email_id.index('@')]


u1 = username('john@xmail.com')
u2 = username('jack@zmail.com')
print(u1, u2)
