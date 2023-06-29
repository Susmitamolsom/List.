n=[4235,7952,6342,500]
i=0
while i<len(n):
    j=0
    sum=0
    b=str(n[i])
    while j<len(b):
       sum=int(b[j])+sum
       j=j+1
    if n[i]%sum==0:
       print(n[i],"is a harshad no. and divisible by",sum)
    else:
       print(n[i],"is not a harshd no. and not divisible by",sum)
    i=i+1

# n=[4235,7952,6342]
# for i in n:
#     sum=0
#     for j in str(i):
#         sum=sum+int(j)
#     if i%sum==0:
#         print(i,"is a harshal no.")
#     else:
#         print(i,"is not a harshal no.")
#     print(sum)