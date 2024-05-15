d = {'raj@xyz.com': {'course': ['Algorithms', 'Painting'], 'city': 'London'},
     'dev@abc.com': {'course': ['Painting', 'Networking'], 'city': 'Delhi'},
     'sam@pqr.com': {'course': ['Design Patterns', 'C', 'C++'], 'city': 'London'},
     'jim@xyz.com': {'course': ['Networking'], 'city': 'Delhi'},
     'pam@abc.com': {'course': ['Algorithms', 'Java'], 'city': 'Delhi'},
     'ray@abc.com': {'course': ['Painting', 'C++'], 'city': 'London'},
     'anu@xyz.com': {'course': ['Algorithms', 'C'], 'city': 'London'},
     'bob@pqr.com': {'course': ['Data Structures', 'Java'], 'city': 'Tokyo'},
     'ted@abc.com': {'course': ['Algorithms', 'C++'], 'city': 'London'},
     'zen@abc.com': {'course': ['Painting'], 'city': 'London'}
     }
d1 = {course for record in d.values() for course in record['course'] if record['city'] == 'London'}
print(d1)
