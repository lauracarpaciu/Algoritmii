nrTel = "74562308BCD"

def validare(numar):
    isVALID = True
    list=[]
    l = [0,1,2,3,4,5,6,7,8,9]
    i =0
    while i in range(0,len(nrTel)):
        for n in nrTel :
            if n not in l:
                isvALID = False

            i += 1
print("Este un nr de tel valid :{}".format(validare(nrTel)))