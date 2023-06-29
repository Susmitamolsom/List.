# n=[1234, 122, 1984, 19372, 100]
# #n=[1234, 922, 1984, 19372, 100]
# i=0
# while i<len(n):
#     a=str(n[0])
#     b=str(n[i])
#     if a[0]==b[0]:
#         match=True 
#     else:
#         match=False
#     i=i+1
# # print(match)

# myscore=1000
# message='i score %s points'
# # print(message%myscore)

# hugehairypants = ['huge', 'hairy', 'pants']
# for i in hugehairypants:
#     print(i)
#     for j in hugehairypants:
#         print(j)

a=16.5
b=0.165
c=a*b
sum=0
year=1
for i in range(1,16):
    sum=c+sum
    print("year=",year,":",sum)
    year=year+1