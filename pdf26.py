# # n=[4,5,5,5,3,8]
n=[2,6,9,2,5,5,5,5,2,1,10]
# i=0
# list=[]
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         if n[i]==n[j] and n[i] not in list:
#             list.append(n[i])
#         j=j+1
#     i=i+1
# print(list)
#n=[1,1,1,64,23,64,22,22,22]
#i=0
#list=[]
#while i<len(n)-2:
#    if n[i]==n[i+1] and n[i+1]==n[i+2]:
#        print(n[i],end=" ")
#    i=i+1

i=0
k=len(n)
a=3
while i<len(n):
    j=0
    count=0
    while j<k:
        if int(n[i])==int(n[j]):
            count=count+1
            if count<a and n[i]==n[j]:
                n=n[i]
            j=j+1
        i=i+1
print(n)