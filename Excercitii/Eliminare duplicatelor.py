# side effect - efecte secundare
[0,4,5,4,2]
[0,5,2]
def removeDuplicates(numbers):
    uniques=[]
    for number in numbers:
        if not uniques.__contains__(number):
            uniques.append(number)

    return  uniques


def removeDuplicateswithHashTable(numbers):

    uniques=[]
    hashTable={}
    for number in numbers:
        if hashTable[number]==None:
            uniques.append(number)
            hashTable[number]=True
    return hashTable
#
print(removeDuplicates([0,2,2,4,4,5,6,7]))
# print(removeDuplicateswithHashTable([0,2,2,4,4,5,6,7]))

def removeDuplicatesUsingSort(numbers):
    sortedNumbers=sorted(numbers)
    uniques=[]
    for i in range(0,len(sortedNumbers)):
        if i is not 0 | sortedNumbers[i-1] is not sortedNumbers[i]:
            uniques.append(sortedNumbers[i])
    return uniques

print(removeDuplicatesUsingSort([0,2,2,4,4,5,6,7]))


