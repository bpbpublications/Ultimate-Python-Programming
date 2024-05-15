d = {'raj@xyz.com': {'course': 'Algorithms', 'city': 'London'},
     'dev@abc.com': {'course': 'Painting', 'city': 'Delhi'},
     'sam@pqr.com': {'course': 'Design Patterns', 'city': 'London'},
     'jim@xyz.com': {'course': 'Networking', 'city': 'Delhi'},
     'pam@abc.com': {'course': 'Algorithms', 'city': 'Delhi'},
     'ray@abc.com': {'course': 'Painting', 'city': 'London'},
     'anu@xyz.com': {'course': 'Algorithms', 'city': 'London'},
     'bob@pqr.com': {'course': 'Data Structures', 'city': 'Tokyo'},
     'ted@abc.com': {'course': 'Algorithms', 'city': 'London'},
     'zen@abc.com': {'course': 'Painting', 'city': 'London'}
     }

d1 = {record['course'] for record in d.values() if record['city'] == 'London'}
print(d1)
