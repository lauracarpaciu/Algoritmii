def bublesort(numbers):
    notSortedyet = True
    while notSortedyet:
        notSortedyet = False
        swaps = 0
        for i in range(0,(len(numbers)-1)):
            if numbers[i]> numbers[i+1]:
                aux = numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=aux
                swaps +=1

        if(swaps>0)  :
            notSortedyet = True


numere = [2,5,3,9,1,4,7]
bublesort(numere)
print("Colectia de numere dupa sortarea cu bublesort:{}".format(numere))