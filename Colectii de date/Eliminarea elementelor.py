# eliminarea elementelor dintr o lista
values = [15,20,-150,25,18,20]
valid = []
i = 0

while i in range(0,len(values)):
    if i not in(2,3):
        valid.append(values[i])
    i += 1

print(valid)