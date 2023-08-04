import json

# file = open("friends.txt", "r")
#
# data = json.load(file)
# file.close()

#           ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

with open('friends.txt', 'r') as file:
    data = json.load(file)

print(data)

# import json
#
# with open("friends.txt", "r") as file:
#     data = json.load(file)
#
# print(data)


# file1 = open("friends1.txt", "w")
# json.dump(data, file1)
# file1.close()

#           ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

with open('friends1.txt', 'w') as file:
    json.dump(data, file)

d = '[{"name": "Anitha", "age": 22}]'

incorrectdata = json.loads(d)

print(incorrectdata[0]['name'])