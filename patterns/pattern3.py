#TRiangle pattern
# n=int(input())
# c=1
# for i in range(1,n+1):
#     print('  '*(n-i),end='')
#     for j in range():
#         print("%02d"%(c),end=' ')
#         c+=1
#     print()

n= int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        if i==1 or j==1 or i==n:
            print('a',end='')
        else:
            print(' ',end=' ')
    print()

        
