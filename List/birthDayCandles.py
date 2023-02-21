n=int(input())
arr=list(map(int,input().split()))
candles=0
k=max(arr)
for i in range(len(arr)):
    if arr[i]>=k:
        candles+=1
print(candles)
    
