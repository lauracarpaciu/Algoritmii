def calcululPretuluicuTrenul(distanta):

    pretul = distanta*1

    return pretul


def calcululPretuluicuAvionul(distanta):

    pretul = distanta*0.5+200

    return pretul

def getCheaperOption(distance):

    costByTrain = calcululPretuluicuTrenul(distance)

    costByPlain = calcululPretuluicuAvionul(distance)

    if costByTrain < costByPlain:

        print("Train")

    else:

        print("Plain")

getCheaperOption(350)