import json

with open("updated_list.json") as json_file:
    words = json.load(json_file)

print(words['10'])
print(words['16'])
print(words['17'])
print(words['18'])
print(words['19'])
