nums=input()
s=""
for i in range (1,len(nums)-1):
    s=s+nums[i]
arr=list(map(int,s.split(",")))


arr.sort()
i=0
j=len(arr)-1
while i<j:
    if arr[i]+arr[j]==t:
        print(i,j,arr[i],arr[j],t)
        break
    elif arr[i]+arr[j]>t:
        j-=1
    else:
        i=i+1

