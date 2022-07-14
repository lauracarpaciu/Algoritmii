matrix = [[110,22,100],[100,103,250],[25,30,20]]
for arr in range(0,len(matrix)):
    max= 0
    for attempt in range(0,3):
        score = matrix[arr][attempt]
        if score>max:
            max=score
    print("Maximul din fiecare array  este:{}".format(max))