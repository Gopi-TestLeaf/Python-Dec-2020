import json

# loads - convert json format to Python format
p_data = json.loads('{"name":"GN", "active": false, "value":null}')
print(p_data)
#*****************************************************************************

# load - read the data from json
with open('samplejson.json', 'r') as file:
    data = json.load(file)
    py = json.loads(data)

print(py)

