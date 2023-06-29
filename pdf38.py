# list=['.com', '.edu', '.tv']
# str='https://www.w3resource.com/python-exercises/list/'
# i=0
# while i<len(list):
#     if list[i] in str:
#         print("true")
#         break
#     else:
#         print("false")
#     i=i+1

list=['.com', '.edu', '.tv']
str='https://www.w3resource.edu/python-exercises/list/'
i=0
while i<len(list):
    if list[i] in str:
        match="true"
    else:
        match="false"
    i=i+1
print(match)