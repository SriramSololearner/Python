a=list(int,input().split())
k=int(input())
InTime=0
for i in range(len(a)):
    if(a[i]<=0):
        InTime+=1
        if(InTime>=k):
            print("NO")
print("YES")