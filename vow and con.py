name=["susmita"]
a=["a","e","i","o","u"]
i=0
l=[]
while i<len(name):
    j=0
    b=[]
    while j<len(name[i]):
        if name[i][j] in a:
            l.append(name[i][j])
        j=j+1
    k=0
    while k<len(name[i]):
        if name[i][k] not in a:
            b.append(name[i][k])
        k=k+1
    i=i+1
print(l,b)