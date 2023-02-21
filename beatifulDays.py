i,j,k = map(int,input().split())
c=0
for i in range(i,j+1):
    d= int(str(i)[::-1])
    if abs(i-d)%k==0:
        c=c+1
print(c)

