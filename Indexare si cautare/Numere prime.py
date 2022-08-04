import _md5
import math


def isPrime(number):
    for i in range(2,int(math.sqrt(number))):
        if number%i==0:
            return False

        return True


print(isPrime(31))


def getnextPrime(primeNumber):
    numbertoCheck=primeNumber*2
    while not isPrime(numbertoCheck):
        numbertoCheck += 1
    return numbertoCheck

print(getnextPrime(13))
print(getnextPrime(29))