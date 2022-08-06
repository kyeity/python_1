import json

with open('name.json') as json_file:
    a = json.load(json_file)

#print(type(a['web-app'] ['servlet']))
for item in a['web-app'] ['servlet']:
    print(item['servlet-name'])