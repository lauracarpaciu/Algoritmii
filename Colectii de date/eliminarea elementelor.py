values = [15,20,-150,25,18,20]
valid = []
i = 0
print(len(values))
while i in range(0,len(values)):
    if i != 2:
        valid.append(values[i])
    i += 1

print(valid)