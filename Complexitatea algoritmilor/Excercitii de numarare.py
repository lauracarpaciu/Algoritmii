varste = [15,20,30,17,24,35,35,35,20,28,40]

def getmostfrequrntage(ages, i=0):
    maxPeoples = 0
    mostFrequrntAge = 0
    buchets = []
    while i <=140:
        buchets.append(0)
        i +=1

    for age in ages:
        buchets[age] +=1
        if buchets[age]> maxPeoples:
            maxPeoples = buchets[age]
            mostFrequrntAge=age

    return mostFrequrntAge

print(getmostfrequrntage(varste))


