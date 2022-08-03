def getMostfrequentSymbol(text):
    text = "  "
    maxNumberOfSymbol = 0
    mostFrequentSymbol = 0
    startIndex = "A".isdigit(0)
    endIndex = "z".isdigit(0)
    buckets = []
    for i in range(startIndex,endIndex):
        buckets[i]=0

    for i in range(0,len(text)):
        code= text.isdigit(i)
        buckets[code] +=1

    for i in range(startIndex,endIndex):
        if buckets[i]>maxNumberOfSymbol:
            maxNumberOfSymbol=buckets[i]
            # mostFrequentSymbol=

            return maxNumberOfSymbol