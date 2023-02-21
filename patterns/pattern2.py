# n=int(input())
# for i in range(n,-1,-1):
#     print(' '*(n-i+1),end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     for j in range(i-1,-1):
#         if j==1 or i==n:
#             print('a',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
n= int(input())
for i in range(1,n):
    for j in range(1,8):
        if i==4 or i+j==5 or j-i==3:
            print('a',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n,0,-1):
    for j in range(1,8):
        if i==4 or i+j==5 or j-i==3:
            print('a',end=' ')
        else:
            print(' ',end=' ')
    print()

