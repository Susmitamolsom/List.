#n=[12,67,98,34]
n=[15,81,11,234]
i=0
l=[]
while i<len(n):
    j=0
    sum=0
    b=str(n[i])
    while j<len(b):
        sum=int(b[j])+sum
        j=j+1
    l.append(sum)
    i=i+1
print(l)