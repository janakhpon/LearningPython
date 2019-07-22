import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"], "__added two year per time \n")
    data["age"] = data["age"]+2
    print("New age is ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name":"Aung Nat", "age":6, "food":"Bone"}
    print("No json file found, so set everything to default and age is ", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
