bin=[1,0,0,1,1,0,1,1]
i=-1
dec=0
p=0
l=-len(bin)
while i>=l:
    if bin[i]==1:
       a=bin[i]
       b=2**p
       c=a*b
       dec=dec+c
    i=i-1
    p=p+1
print(dec)