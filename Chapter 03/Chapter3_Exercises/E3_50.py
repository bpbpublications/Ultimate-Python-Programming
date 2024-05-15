email_id = input('Enter an email id - ')
username = email_id[:email_id.index('@')]
domain_name = email_id[email_id.index('@') + 1:]
print(username)
print(domain_name)
