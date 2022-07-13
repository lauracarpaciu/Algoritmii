def getavarage(values):
    values.sort()
    start = 2
    end = len(values)-2
    suma =0
    for index in range(start,end):
        suma += values[index]
        average = suma/(len(values)-4)
        return average


valori = [20,21,23,25,19,20,26,2000000,20000]
print(getavarage(valori))