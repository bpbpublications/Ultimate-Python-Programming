
def username(email_id):
    """Returns the username from an email id"""
    return email_id[:email_id.index('@')]


u1 = username('john@xmail.com')

print(username.__name__)
print(username.__doc__)
print(username)

