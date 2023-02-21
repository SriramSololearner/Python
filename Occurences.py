# l=[2,3,7,8,9,2,4,2,6,3,1,6,2]
# k=6
# x=0
# while k in l[x:]:
#     if k==x:
#         l.index(k,x)
#         print(x)
# x+=1
# y=int(input())
# ind=[int(i) for i,x in enumerate(l) if x==y]
# print(ind)

l=[2,3,7,8,9,2,4,2,6,3,1,6,2]
k=int(input())
for i,v in enumerate([1,2,3,4,5,6,8,9,8,9,5,6,4,7,8,9,5,4,6,3,6,8,5,2,3,6,9,8,7,4,5,5,2]):
    if v==k:
        print(i)
