list = [ 1990,2005,1997,2002,2010]

def numarare (numbers, numar=0, num=0):
    for num in numbers:
       if (2022-num ) >= 18:
            numar +=1
    return numar

print(numarare(list))