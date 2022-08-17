numerePlacuteinmatric = ["IS 43 ABC", "CJ 20 EFG", "B 101 EZC" , "CJ 30 XYZ"]
i =0
l=[]
while i in range(0,len(numerePlacuteinmatric)):
    for n in numerePlacuteinmatric:
        country = n[0:2]
        print(country)
        i += 1
        if "CJ"==country:
            l.append(country)
print("Numarul judetului CJ este {}".format(l.count("CJ")))
