# n = int(input())
# arr=[int(i) for i in input().split()]
# positive=[]
# negative=[]
# zero=[]
# for i in range(len(arr)):
#     if arr[i]>0:
#         positive.append(arr[i])

#     elif arr[i]<0:
#         negative.append(arr[i])

#     elif arr[i]==0:
#         zero.append(arr[i])

# print('{:.6f}'.format(len(positive)/len(arr)))
# print('{:.6f}'.format(len(negative)/len(arr)))
# print('{:.6f}'.format(len(zero)/len(arr)))

n = int(input())
arr=[int(i) for i in input().split()]
pos=neg=zero=0
for i in range(len(arr)):
    if arr[i]>0:
        pos+=1
    elif arr[i]<0:
        neg+=1
    else:
        zero+=1
print('{:.6f}'.format(pos/n))
print('{:.6f}'.format(neg/n))
print('{:.6f}'.format(zero/n))






