def isDigit(character):
    return "0" <= character and character <='9'

def isLetter(character):
    upper = "A" <= character and character <= 'Z'
    lower =  "a" <= character and character <= 'z'
    return upper | lower

print(isDigit("5"))
print(isLetter("7"))