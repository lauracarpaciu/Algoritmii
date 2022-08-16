def powIterative(x,y):
    result=1

    for i in range(1,y+1):
        result=result*x

    return result
print((powIterative(5,3)))

# def pow(x,y):
#     # if y == 0:
#     #     return 1
#     # if y == 1:
#     #     return x
#     halfPow=pow(x,float(y/2))
#
#     if y%2==0:
#         return halfPow*halfPow
#     else:
#         return x*halfPow*halfPow
#
# print(pow(5,3))