import math

def extractdigit(numar):
    digits = []
    while numar>0:
        lastDigit = numar%10
        numar = math.floor(numar/10)
        digits.append(lastDigit)
    return digits

def mergeDigits(digits):
    numarulformat =0
    for digit in digits:
        numarulformat =numarulformat*10+digit

    return numarulformat

def getnumber(numar):
    digits = extractdigit(numar)
    digits.sort()
    maxDigit=mergeDigits(digits)
    return maxDigit
print(mergeDigits([4,3,25]))

print(mergeDigits(extractdigit(234569)))
numar = 2356999
print(getnumber(numar))

