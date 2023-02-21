arr=[1, 3, 2, 6, 1, 2]
k=5
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            if(arr[i]+arr[j])%k==0:
                count+=1
print(count)

