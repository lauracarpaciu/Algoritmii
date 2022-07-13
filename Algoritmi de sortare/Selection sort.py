
def sort(numbers):
    for i in range(0, len(numbers)-1):
       for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                aux = numbers[i]
                numbers[i]=numbers[j]
                numbers[j]=aux

numbers = [25,2,8,-6,4,3,2]
print("Colectie de numere nesortate:{}".format(numbers))
sort(numbers)
print("Colectie de numere dupa aplicarea algoritmului de sortare:{}".format(numbers))