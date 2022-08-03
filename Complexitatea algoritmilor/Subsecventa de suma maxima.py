numbers =[6,-8,3,2,-2,7,8,9]

bestSum1=0
bestsStart1=0
bestEnd1 = 0

for start in range(0,len(numbers)):
    for end in range(start,len(numbers)):
        sum =0
        for i in range(start,end):
            sum =sum + numbers[i]
            if sum > bestSum1:
                bestSum1=sum
                bestsStart1=start
                bestEnd1=end


print("Secventa de suma maxima {} cu {} start si {} end".format(bestSum1,bestsStart1,bestEnd1))
