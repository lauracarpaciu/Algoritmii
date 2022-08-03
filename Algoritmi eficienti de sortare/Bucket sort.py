def getBucketIndex(persons):
    age=persons.age
    if age>49:
        return 4
    if age>49:
        return 4
    if age>49:
        return 4
    if age>49:
        return 4
    return 0
def bucketSort(persons):
    numberOfBuckets = 5
    buckets=[]


    for i in range(0,5):
      buckets.append([])

    for person in persons:
        bucketIndex = getBucketIndex(person)
        bucket=buckets[bucketIndex]

    for bucket in buckets:
        for person in bucket:
            print(person.name,person.age)

persons=[{'name':"Ion",'age':35},

         {'name': "Ion", 'age': 35} ]
bucketSort(persons)