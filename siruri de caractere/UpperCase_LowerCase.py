destination = "bUCURESTI"

primaLitera = destination[0]
urmatoareleLitere = destination[1:len(destination)]


upper=primaLitera.capitalize()
lower = urmatoareleLitere.lower()
concat = upper + lower
print("Am rescris stingul destination :{} ".format(concat))