# a=[1,2,3]
# b=["one","two","three"]
# i=0
# l=[]
# while i<len(a):
#     c=a[i]
#     d=b[i]
#     l.append(c)
#     l.append(d)
#     i=i+1
# print(l)



l=[1,2,5,4,5,6,7,8]
i=-1
a=-len(l)
while i>=a:
    if l[i]==l[-4]:
       i=i-1
print(l[-4])