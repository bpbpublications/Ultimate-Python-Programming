from functools import wraps


def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} called')
        print(f'args : {args}  kwargs : {kwargs}')
        result = fn(*args, **kwargs)
        print(f'Return value : {result}\n')
        return result

    return wrapper


@trace
def username(email_id):
    """Returns the username from an email id"""
    return email_id[:email_id.index('@')]


u1 = username('john@xmail.com')

print(username.__name__)
print(username.__doc__)
print(username)
