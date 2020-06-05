import json

userJSON ='{"first_name":"john","last_name":"Doe","age":30}'

user=json.loads(userJSON)

print(user)