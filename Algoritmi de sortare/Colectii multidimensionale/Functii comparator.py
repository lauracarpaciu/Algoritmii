people = [
{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},

{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
]


def compareByAgeAscend(personA,personB):
    if personA.year < personB.year:
        return -1
    if personA.year == personB.year:
        return 0

    if personA.year > personB.year:
        return 1


print(people.sort(compareByAgeAscend))

arr =[12,10,13,20,22]

def comparareNumere(numA,numB):
    return numA-numB

print(arr.sort(comparareNumere))
