num=[[8,3,4],
     [1,5,9],
     [6,7,2]]
# r=0
# i=0
# while i<len(num):
#     j=0
#     while j<len(num[i]):
#         r=r+num[i][j]
#         j=j+1
#     i=i+1
# print(r)
# i=0
# c=0
# while i<len(num):
#     j=0
#     while j<len(num[i]):
#         c=c+num[j][i]
#         j=j+1
#     i=i+1
# print(c)
# d=0
# dig=0
# while d<len(num):
#     f=0
#     while f<len(num[d]):
#         if d==f:
#            dig=dig+num[d][f]
#         f=f+1
#     d=d+1
# print(dig)
g=0
k=-1
dig2=0
while g<len(num):
    dig2=dig2+num[g][k]
    k-=1
    g=g+1
print(dig2)
# if r==c and dig==dig2:
#     print("it is a magic square")
# else:
#     print("its not magic square")