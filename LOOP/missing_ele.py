
# arr = [1,2,3,4,6]
# sum =0
# for i in range(0,len(arr)):
#     sum+=arr[i]
# n=arr[-1:][0]
# sum2=n*(n+1)/2
# print(int(sum2-sum))

arr= [1,2,3,5,6,8]              
m=[]                                          
for i in range(arr[0],arr[-1]+1):                   #1 8
    if i not in arr:                          #i=1  1                                
        m.append(i)
print(arr,m)
