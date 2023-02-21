n=int(input())
mm=mx=0
l=list(map(int,input().split()))
mp=lp=l[0]
for i in l:
    if i>mp:
        mx=mx+1
        mp=i
    elif i<lp:
        mm=mm+1
        lp=i
print(mx,mm)