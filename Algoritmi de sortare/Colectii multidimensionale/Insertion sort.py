def getInserPosition(elem, arr):
   if len(arr)==0:
    return 0

    for i in range(0,len(arr)):
        if elem <= arr[i]:
            return i

    return len(arr)-1

def moveElemenToRight(arr,start):
    for i in range(len(arr),-1):
        print(i)
        # if i > start:
        #     arr[i]=arr[i-1]


def insertationSort(numbers):
    sortedArr = []
    for number in numbers:
        pos = getInserPosition(number,sortedArr)
        # moveElemenToRight(sortedArr,pos)
        sortedArr[pos]= number

    return sortedArr
numbers =[20,56,23,1]
insertationSort(numbers)
print(insertationSort(numbers))