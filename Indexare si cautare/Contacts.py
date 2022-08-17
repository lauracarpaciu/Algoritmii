class MyContacts:
    def __init__(self, hashTable={}):
        self.hashTable = hashTable

    def get(self,name):
        return self.hashTable[name]
    def add(self,name,phoneNumber):
        previousValue= self.get(self, name)
        if not previousValue:
            self.hashTable[self.name]=[phoneNumber]
        elif previousValue is phoneNumber:
               print("{} are deja numarul".format(self.name))


MyContacts.add("ion","0726376","23333")
MyContacts.add("ion","072637629")