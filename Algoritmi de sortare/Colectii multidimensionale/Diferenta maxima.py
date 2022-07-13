def getmaxdiff(values):
    maxDiff = 0
    values.sort()
    for i in range(0,len(values)-1):
        diff = values[i+1]- values[i]
        if diff>maxDiff:
            maxDiff = diff
    return maxDiff


print(getmaxdiff([20,56,20,59,10,500]))