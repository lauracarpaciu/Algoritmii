def getNumberOfCoins(S):
    coins=sorted([1,5,10,50,100])
    usedCoins=[0,0,0,0,0]
    largestCoinsIndex=4
    while S > 0:
        largestCoinsValue = coins[largestCoinsIndex]

        if S >= largestCoinsValue:
            S = S-largestCoinsValue
            usedCoins[largestCoinsIndex] += 1
        else:
            largestCoinsIndex -= 1

    return usedCoins


print(getNumberOfCoins(375))
