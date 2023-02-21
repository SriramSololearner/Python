num = int(input("Enter a number: "))
flag = False

# check if num is equal to 7^n
for i in range(1, num+1):       
    if 7**i == num:   # 7^2
        flag = True

# check if flag is set
if flag :
    print(num, " is Yes")
else:
    print(num, "is NO")

# n=int(input())
# c=0
# for i in range(1,n+1):
#     8**i==n
#     c+=1
# if c==1:
#     print('yes')
# else:
#     print('No')