def getAbsDiff(numbers):
    numbers=sorted(numbers)
    min=999999
    for i in range(0,len(numbers)-1):
        number=numbers[i]
        nextNumber=numbers[i+1]
        absDiff=abs(nextNumber-number)
        if absDiff<min:
            min=absDiff
    return min

print(getAbsDiff([0,-3,5,6,10,20,30,18]))