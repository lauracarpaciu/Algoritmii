def countingSort(numbers):
    counters = []
    maxPossibleValues = 100
    for i in range(0,maxPossibleValues+1):
        counters.append(0)

    for number in numbers:
        counters[number] +=1

    for key in range(0,maxPossibleValues+1):
        ocurrences=counters[key]
        for i in range(1,ocurrences+1):
            print(key)

countingSort([1,3,2,1,0,44,22,11])