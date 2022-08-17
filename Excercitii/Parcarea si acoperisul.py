def getMinRoofLenght(spotsWithCars,X):
    spotsWithCars=sorted(spotsWithCars)
    minLenght=99999

    for start in range(0,len(spotsWithCars)-X+1):
        end=start+X-1
        lenght=spotsWithCars[end]-spotsWithCars[start]+1

        if lenght< minLenght:
            minLenght=lenght

    return minLenght

print(getMinRoofLenght([2,4,6,7,8,1,15,20],4))