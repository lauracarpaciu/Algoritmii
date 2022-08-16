# [1,5,2,10,6,4,3]
# for number in numbers:
#     pair = p/number
#     if pair is in hashTable:
#         print(number,p)
#         hashTable.append(number)

def findPairs(numbers,P):
    for i in range(0,len(numbers)-1):
        for j in range(i,len(numbers)):
            firstNumber=numbers[i]
            secondNumber=numbers[j]
        if firstNumber*secondNumber==P:
            print("Found {}".format(firstNumber),"Found {}".format(secondNumber))


findPairs([1,2,3,4,6],12)

def findPairswithHashTable(numbers,P):
    hashTable={}
    for number in numbers:
        possiblePair = int(P/ number)

        if hashTable.get(possiblePair) is not None:
            print("Found {}".format(number),"Found {}".format(possiblePair))
        hashTable[possiblePair]=True


findPairswithHashTable([1,5,2,10,6,4,3],12)

def findPairsBySortedArray(numbers,P):
    sortedNumbers=sorted(numbers)

    left=0
    right=len(sortedNumbers)-1
    while left < right:
        firstNumber=sortedNumbers[left]
        secondNumber=sortedNumbers[right]
        currentProduct=firstNumber*secondNumber

        if currentProduct==P:
            print("Found {}".format(firstNumber),"Found {}".format(secondNumber))

        if currentProduct > P:
            right -= 1
        else:
            left += 1


findPairsBySortedArray([1,5,2,10,6,4,3],12)