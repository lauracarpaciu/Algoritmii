
lista = [2500,1800,1500,2000,2400]


def Filtrare(numbers ,num=0,list=[]):
    for num in numbers:
        if num < 2400:
            list.append(num)
        return list


print(Filtrare(lista))

