#
# nume = ["Popescu","Georgescu","Ioescu"]
# ages = [26,35,29]

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ionescu", 32)
print(p1.name)

persons = [
  (
    "Ion",
    36
  ),
    ("Ion", 63),
    ("Ion",29 ),
]
persons.append( ("Ion",29 ))

for p in persons:
    for i in p:
        print(i)
    try:
        i = int(i)
        if i <= 29:
            print ("Ion are :{}".format(i))
    except ValueError:
        print(" could not convert string to int!")