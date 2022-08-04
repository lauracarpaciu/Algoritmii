def findPivot(values, start,end):
    left = start
    right = end
    order = True
    while left<right:
        if values[left]>values[right]:
            aux = values[left]
            values[left]=values[right]
            values[right]=aux
            order !=order

        if order==True:
            left +=1
        else:
            right -=1


    return left

def quickSort(values,start,end):
    if start > end:
        return
    pivot = findPivot(values,start,end)
    quickSort(values,start,pivot-1)
    quickSort(values,pivot + 1,end)

numbers = [2,5,69,23,56]
print(quickSort(numbers,start=0,end=len(numbers)-1))
print(numbers)