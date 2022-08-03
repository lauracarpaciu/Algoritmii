import math


def binarySearch(values,needle):
    start=0
    end=len(values)-1
    found=False
    while not found and start<=end:
        middleIndex = math.floor((start+end)/2)
        middleValue = values[middleIndex]
        if needle == middleValue:
            found =True
        elif needle<middleValue:
            end=middleIndex
        else:
          start=middleIndex+1

    return found
print(binarySearch([2,3,4,5,6,7,8,9,10],11))