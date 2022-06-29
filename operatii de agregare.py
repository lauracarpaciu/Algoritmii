
list = [15,30,20,16,22,18]
def total(numbers, total=0):
    for i in numbers:
        total += i
    return total

print(total(list))

list2 = [32,26,28,29,30]
def medie(elem, total=0):
    for i in elem:
        total += i
        medie = total/len(elem)
    return medie

print(medie(list2))

