def calculatePriceByTrain(distance):
    cost = distance*1
    return cost

def calculatePriceByPlain(distance):
    cost = distance*0.5+200
    return cost

def getCheaperOption(distance):
    costByTrain=calculatePriceByTrain(distance)
    costByPlain = calculatePriceByPlain(distance)

    if costByTrain<costByPlain:
        print("Train")
    else:
        print("Plain")

getCheaperOption(350)