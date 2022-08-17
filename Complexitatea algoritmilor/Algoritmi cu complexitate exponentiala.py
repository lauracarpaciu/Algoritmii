import random

numbers = 100
numere = []
for i in range(0,100):
    numere.append(random.random()*1000)


print(numere)

for i in range( 0, len(numere)-1):
    for j in range(i+1,len(numere)):
        if numere[i]>numere[j]:
            aux = numere[i]
            numere[i]=numere[j]
            numere[j]=aux

print("Dupa aplicarea algoritmului de sortare avem:{}".format(numere))