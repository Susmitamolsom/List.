l=int(input("enter"))
i=0
k=[]
while i<l:
    e=int(input("enter"))
    j=0
    k.append(e)
    while j<len(k):
        if k[i]<k[j]:
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
        j=j+1
    i=i+1
print(k)

# a=int(input("enter"))
# b=str(a)
# i=0
# sum=0
# even=0
# while i<len(b):
#     j=0
#     while j<len(b[i]):
#         if int(b[i][j])%2==0:
#             sum=sum+(int(b[i][j]))
#             even=even+1
#         j=j+1
#     i=i+1
# avg=sum/even
# print(avg)

# l=int(input("enter"))
# b=str(l)
# i=0
# k=[]
# while i<len(b):
#     j=0
#     while j<len(b[i]):
#         k.append(b[i][j])
#         k.sort()
#         j=j+1
#     i=i+1
#print(k)