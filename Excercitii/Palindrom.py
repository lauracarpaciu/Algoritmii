
def isPalindromReverse(sir):
    reverse =''

    for i in range(len(sir)-1,-1):
        reverse=reverse+sir[i]
    return sir==reverse

# print(isPalindromReverse("capac"))

def isPalidromBothDirections(str):
    left=0
    right=len(str)-1

    while left<right:
        if str[left]!=str[right]:
            return False

        left +=1
        right -=1
    return True

print(isPalidromBothDirections("capac"))