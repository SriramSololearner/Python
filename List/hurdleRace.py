n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
x=max(l)
if x>k:
    print(x-k)
else:
    print(0)