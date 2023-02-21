n,k=map(int,input().split())
num=int(str(n)*k)
while num>9:
    s=0
    while num!=0:
        d=num%10
        s=s+d
        num=num//10
    num=s
print(num)