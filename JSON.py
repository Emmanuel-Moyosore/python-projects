import json
x= {
    'name':'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'Children':('Ann','Billy'),
    'pets':None,
    'cars':[
        {'model': 'BMW 230','mpg':27.5},
        {'model': 'Ford Edge', 'mpg': 24.1}
        ]
    }
# Convert into JSON
y= json.dumps(x)
# The result is a JSON STRING:
print(y)



# to sort the results alphabetically by keys
import json
x= {
    'name':'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'Children':('Ann','Billy'),
    'pets':None,
    'cars':[
        {'model': 'BMW 230','mpg':27.5},
        {'model': 'Ford Edge', 'mpg': 24.1}
        ]
    }
print(json.dumps(x, indent=4, sort_keys = True))


import json
x= {
    'name':'John',
    'age': 30,
    'married': True,
    'divorced': False,
    'Children':('Ann','Billy'),
    'pets':None,
    'cars':[
        {'model': 'BMW 230','mpg':27.5},
        {'model': 'Ford Edge', 'mpg': 24.1}
        ]
    }
print(json.dumps(x, indent=4, separators=(",",":")))

