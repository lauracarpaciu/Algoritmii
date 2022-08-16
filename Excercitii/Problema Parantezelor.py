def isCoressponding(opening, closing):
    if opening=='(':
        return closing==")"
    elif  opening=='{':
        return closing == "}"
    else:
        return closing =="]"

    return False
def isOpening(character):
    openingPharantese=['[','{','(']
    return openingPharantese.__contains__(character)


def isCorrect(str):
    stack=[]
    size=0
    for i in range(0,len(str)-1):
        character=str[i]
        if isOpening(character):
            stack.append(character)
            size += 1
        else:
            if size==0:
                return False

        lastCharacterInStack = stack[size-1]
        if not isCoressponding(lastCharacterInStack,character):
            return False
        else:
            size +=1
    return  size==0

print(isCorrect('[][))])'))
print(isOpening("("))
print(isCoressponding("(",")"))