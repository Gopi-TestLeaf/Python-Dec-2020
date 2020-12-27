p_data = {
    'name': 'Gopinath',
    'value': None,
    'is_Nothing': True,
    'hobbies': ('always sleeping', 'always eating'),
    'pay': 000
}
print(type(p_data))

import json

# dumps - convert python to json

j_data = json.dumps(p_data, indent=4)
print(type(j_data))

print(j_data)

# dump - write to json file
with open('samplejson.json', 'w') as file:
    json.dump(j_data, file, indent=4)

