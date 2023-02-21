arr=[[11,2,4],[4,5,6],[10,8,-12]]
leftD = 0
rightD = 0
for i in range(0,len(arr)):
    
    leftD += arr[i][i] 
    # print(leftD,arr[i][i])
for j in range(0,len(arr)):
    rightD += arr[j][len(arr)-j-1]
print(abs(rightD-leftD))



# print(len(arr))
# print(arr[-1])
