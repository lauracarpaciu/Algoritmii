def hasonlywins(outcomes, left, right):
    for index in range(left,right):
        if outcomes[index]!="W":
            return False
    return True

def ceamailungasecvdevict(outcomes):
    mostwins = 0
    for left in range(0,len(outcomes)):
        for right in range(left, len(outcomes)):
            if hasonlywins(outcomes,left,right):
                wins = right - left
                if wins > mostwins:
                    mostwins=wins

    return mostwins


result = ["L","W","W","W","D"]
print("Cea mai lunga secventa de victorii:{}".format(ceamailungasecvdevict(result)))