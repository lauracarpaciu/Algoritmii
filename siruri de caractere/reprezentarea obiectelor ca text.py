price = [12.5,12,30]
print("Pretul este : {}".format(price))
product = {
        'nume':"tv",
           'price': 1200
           }
print(product.items())

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + '' + self.name