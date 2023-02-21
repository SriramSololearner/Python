
 
# n=int(input())
# for i in range(1,n+1):
#     print('  '*(n-i)+'*'*i)        
# for j in range(n,0,-1):
#     print(' '*(n-j)+'*'*j)

n=int(input())
for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()    
for i in range(n-1,0,-1):
    print('  '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()

#diamond upper part
# n=int(input())
# for i in range(1,n+1):
#     print('  '*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     for j in range(i-1,0,-1):
#         print(j,end=' ')
#     print()
#diamond down part
# n=int(input())
# for i in range(n-1,0,-1):
#     print('  '*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     for j in range(i-1,0,-1):
#         print(j,end=' ')
#     print()


