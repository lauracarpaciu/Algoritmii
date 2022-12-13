temp = [9.0, 8.8, 8.9 , 9.2 , 9.0]

def MIN(numbers, minimum = 99999):
    l=[]
    for num in numbers:
         if num < minimum:
             minimum = num

    return minimum

print(MIN(temp))