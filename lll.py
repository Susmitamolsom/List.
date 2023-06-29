a=[1,[[2]],[3,4,5],'6']
print(a[0],a[1][0],a[2][1:])

# a=[1,[[2]],[3,4,5],'6']
# a[1]=a[1][0][0]
# a=a+a[2]
# a.append(int(a[3]))
# del a[2:4]
# print(a)


# temp=['a','b','c','d','e']
# def dummy(temp):
#     i=0
#     while i<len(temp):
#         if temp[i]<=temp[i+1]:
#             if i==len(temp)-1:
#                 print("code is ascending order")
#         else:
#             print("false")
#             break