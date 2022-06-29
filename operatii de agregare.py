
list = [15,30,20,16,22,18]
def total(list, total=0):
    for i in list:
        total += i
    return total

print(total(list))