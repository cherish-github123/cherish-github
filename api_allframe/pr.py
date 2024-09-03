import json

data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
print(type(data))


json_data=json.dumps(data)
print(type(json_data))

new_data=json.loads(json_data)
print(type(new_data))