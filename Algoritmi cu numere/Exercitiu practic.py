def calculateTimeByByke(distance):
    time=distance/15
    return time

def calculateTimeByCar(distance,departureTime):
    speed=0
    if departureTime in (9,19):
        speed=10
    else:
        speed=30

    time=distance/speed

    return time
def calculateShortestTime(distance,departureTime):
    timeByByke=calculateTimeByByke(distance)
    timeByCar=calculateTimeByCar(distance,departureTime)

    if timeByByke<timeByCar:
        bestTime=timeByByke
    else:
        bestTime=timeByCar
    bestTimeinMinutes=bestTime*60
    return bestTimeinMinutes

print(calculateShortestTime(5,7))

print("-----------------------------------")

