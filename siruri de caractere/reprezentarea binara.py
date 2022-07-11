import json


class Person:
    def __init__(self, price, name):
        self.price = price
        self.name = name

 # set de reguli, format de serializare a datelor - json(java script object notation)
# person =Person("ionescu", 2000) - > serializat -> String(format json) -> transmise prin internet, fisiere, hard extern -> obiecte(deserializare)

thisdict = [
    { "brand": "Ford",
    "model": "Mustang",
    "year": 1964},

            {"brand": "Ford",
             "model": "Mustang",
             "year": 1964}
]

print(thisdict)

# convert into JSON:
y = json.dumps(thisdict)
print("Serializarea:{}".format(y))

# scriere date intru fisier, dupa serializarea
f = open("demofile2.txt", "a")
f.write(y)
f.close()

# parse x:
x = json.loads(y)
print("Deserializarea:{}".format(x))