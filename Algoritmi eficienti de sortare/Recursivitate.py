def recursiveBinarySearch(x,sortedArray,start,end):
    if start > end:
        return False

    middle = int((start+end)/2)

    if x == sortedArray[middle]:
        return True

    if x> sortedArray[middle]:
        return recursiveBinarySearch(x,sortedArray,middle+1,end)
    else:
        recursiveBinarySearch(x,sortedArray,start,middle-1)


print(recursiveBinarySearch(10,[10,20,30,40,50],0,4))