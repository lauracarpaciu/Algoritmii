list=[20,30,20,35,56,98]
# count
def count(list,count=0):
    for i in range(0,len(list)):
        if list[i] < 35:
            count += 1
    return ("valaoare este {}".format(count))

print(count(list))

# add

def add(list, newList=[]):
    for i in range(0,len(list)):
        newList.append(list[i])
    return newList

print(add(list))

def isPresent(list):
    for i in range(0,len(list)):
        if list[i]<=56:
            return True
        else:
            return False

print(isPresent(list))

def isPresent2(list):
    i = len(list)-1

    while i >= 0:
        if list[i] <= 20:
            return True
        i -=1

print(isPresent2(list))

def findMin(list,min=99999):
    for i in range(0,len(list)):
        if list[i]<min:
            min=list[i]
            return min
print(findMin(list))