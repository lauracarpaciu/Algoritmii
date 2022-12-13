# operatii de agregare: media si suma elem din lista

list = [15,30,20,16,22,18]

def Total(numbers, total=0):
    for i in numbers:
        total += i
    return total

print(Total(list))

list2 = [32,26,28,29,30]

def Medie(elem, total=0):
    for i in elem:
        total += i
        medie = total/len(elem)
    return medie

print(Medie(list2))

