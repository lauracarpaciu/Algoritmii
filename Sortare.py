
# Operatiuni de sortare a unei liste

numere = [2,5,3,9,1,4,7]

def bubbleSort(numere):

    notSortedyet=True

    while notSortedyet:
      swaps=0
      notSortedyet = False

      for i in range(0,(len(numere)-1)):
        if numere[i] > numere[i+1]:
          aux=numere[i]
          numere[i]=numere[i+1]
          numere[i+1]=aux
          swaps +=1

        if swaps > 0:
          notSortedyet =True

# bubbleSort(numere)
# print(numere)

# Selection sort
def selectionSort(list):
    lista=[]
    for i in range(0,len(list)-1):
        for j in range(i , len(list)):
            if list[i]>list[j]:
                aux = list[i]
                list[i]=list[j]
                list[j]=aux

# selectionSort(numere)
# print(numere)

def countingSort(list):
    counters=[]
    maxPossValue=20
    for i in range(0,maxPossValue+1):
        counters.append(0)
        print(counters)

    for l in list:
     counters[l] += 1
     print(counters)

    for key in range(0,maxPossValue+1):
        ocurrences=counters[key]
        for i in range(1,ocurrences+1):
            print(key)


# countingSort(numere)
# print(countingSort(numere))

# Quick sort

def findPivot(list,start,end):
    left = start
    right = end
    order=True
    while left < right:
        if list[left]>list[end]:
            aux = list[left]
            list[left]=list[right]
            list[right]=aux
            order!=order

        if order==True:
            left += 1
        else:
            right -= 1

    return left

def quickSort(list,start,end):

    if start > end:
        return

    pivot=findPivot(list,start,end)
    quickSort(list,start,pivot-1)
    quickSort(list,pivot+1,end)


# quickSort(numere,0,len(numere)-1)
# print(numere)

# Operatiuni de a atata prezenta unui element intr o lista

perechi=[1,5,2,10,6,4,3]

def findPairBySortedArray(list,left,right,P=0):
    list=sorted(list)
    left=0
    right=len(list)-1

    while left < right:
        firstNr=list[left]
        secondNr=list[right]
        curentNr=firstNr*secondNr

        if curentNr == P:
            print("found")
        if curentNr > P:
            right -= 1
        else:
            left += 1
findPairBySortedArray(perechi,0,7,12)

sortedArr=[10,20,30,40,50]

# Operatiune de cautare a prezentei unui element dat, intr o lista
def recursiveBinarySearch(x,sortedArr,start,end):
    if start > end:
        return False

    middle=int((start+end)/2)

    if x == sortedArr[middle]:
        return True
    if x > sortedArr[middle]:
        return recursiveBinarySearch(x,sortedArr,middle+1,end)
    else:
        return recursiveBinarySearch(x,sortedArr,start,middle-1)

a=recursiveBinarySearch(20,sortedArr,0,len(sortedArr))
print(a)

# Operatiune de cautare a unui segment intr o lista

result = ["L","W","W","D"]
def hasonlyWins(list,left,right):
   for i in range(left,right):
       if list[i]!="W":
           return False
   return True

def mostWins(list):
    mostWin=0
    for left in range(0,len(list)):
        for right in range(left,len(list)):
            if hasonlyWins(list,left,right):
                wins=right-left
                if wins>mostWin:
                    mostWin=wins
    return mostWin


print(mostWins(result))

# Operatiuni de eliminare a elementelor ce se repeta in interiorul unei liste

duplicate = [0,2,2,4,4,5,6,7]
def removeDuplicateswithHashTable(numbers=[]):
    uniques=[]
    hashTable={}

    for number in numbers:
        if hashTable.get(number)==None:
            uniques.append(number)
            hashTable[number]=True

    return uniques

print(removeDuplicateswithHashTable(duplicate))

# Obtinerea unei liste dintr un numar
def getNBofCoins(S):
    coins=sorted([1,5,10,50,100])
    usedCoins=[0,0,0,0,0]
    Index=len(coins)-1
    while S > 0:
        if S >= coins[Index]:
            S=S-coins[Index]
            usedCoins[Index] +=1
        else:
            Index -=1
    return usedCoins
print(getNBofCoins(375))


