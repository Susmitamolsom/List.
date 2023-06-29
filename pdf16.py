n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
j=1
k=[]
while i<len(n):
    a=n[i]
    count=0
    if j<len(n):
        b=n[j]
        while a<b:
            count=count+1
            a=a+1
        k.append(count)
    j=j+1
    i=i+1
print(k)