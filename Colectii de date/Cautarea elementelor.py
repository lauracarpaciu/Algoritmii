# cautam daca yn element este prezent(absent) in lista,si returnam True/False

years = [2111,2011,2010,2012,2015,2020,2014]
l = []
# for i in years:
#     print(i)
#     if i <= (2021 - 8):
#         l.append(i)
#
# print(l)

def hasInput(years):
     for i in years:
        # print(i)
        if i <= (2021 - 8):
            return True
        return False


print(hasInput(years))