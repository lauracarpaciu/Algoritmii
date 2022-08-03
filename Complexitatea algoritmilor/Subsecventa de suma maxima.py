numbers =[6,-8,3,2,-2,7,8,9]

bestSum1=0
bestsStart1=0
bestEnd1 = 0

for start in range(0,len(numbers)):
    for end in range(start,len(numbers)):
        sum =0
        for i in range(start,end+1):
            sum += numbers[i]
            if sum > bestSum1:
                bestSum1=sum
                bestsStart1=start
                bestEnd1=end


print("Secventa de suma maxima {} cu {} start si {} end".format(bestSum1,bestsStart1,bestEnd1))

bestSum2=0
bestsStart2=0
bestEnd2 = 0

for start in range(0,len(numbers)):
    currentSum=0
    for end in range(start,len(numbers)):
        currentSum +=numbers[end]

        if currentSum>bestSum2:
            bestSum2=currentSum
            bestsStart2=start
            bestEnd2=end


print("Secventa de suma maxima {} cu {} start si {} end".format(bestSum2, bestsStart2,bestEnd2))
bestSum=0
bestStart=0
bestEnd=0
start = 0
currentSum=0
for end in range(-len(numbers),0):
    currentSum=currentSum+numbers[end]
    if currentSum<0:
        start=end+1
        currentSum=0
    elif currentSum>bestSum:
        bestSum=currentSum
        bestStart=start
        bestEnd=end

print("Secventa de suma maxima {} cu {} start si {} end".format(bestSum, bestStart, bestEnd))
