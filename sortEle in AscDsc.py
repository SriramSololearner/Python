# sorting first k elements in Ascending order and remaining Descending order
l=[9,6,5,4,5,2,3,4,5,6,1,2,6,5,7,8,6,3,1,3]
# k=int(input())
# x=l[k:]
# y=l[:k]
# x.sort()
# y.sort(reverse=True)
# print(x+y)
k=int(input())
As=[]
Ds=[]
for i in range(len(l)):
    if i<k:
        As.append(l[i])
    else:
        Ds.append(l[i])
As.sort()
Ds.sort(reverse=True)
print(As+Ds)

