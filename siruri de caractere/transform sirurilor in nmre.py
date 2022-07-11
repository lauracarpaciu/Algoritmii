# suma = input("Introduceti suma in lei :")
# curs = input("Introduceti cursul zilei:")
# suma = float(suma)
# curs = float(curs)
#
# euro= suma/curs
# print("Valoarea in euro este:{}".format(euro))

try:
    suma = float(input("Introduceti suma in lei :"))
    curs  = float(input("Introduceti cursul zilei :"))
    euro= suma/curs
    print("Valoarea in euro este:{} euro".format(euro))
except ValueError:
    print (" could not convert string to int!")


# class ValueError(Exception):

