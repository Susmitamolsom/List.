name=input("enter")
i=0
while i<len(name):
    a=name[i]
    i=i+1
b=-1
c=-len(name)
while b>=c:
    d=name[b]
    print(d)
    b=b-1
if a==d:
    print("palindrome")
else:
    print("not palindrome")