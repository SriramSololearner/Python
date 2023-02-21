# n=int(input())
# l=[int(i) for i in input().split()]
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# l=sorted(list(d.items()), key=lambda x:x[1], reverse=True)
# print(l[0][0])

# n=int(input())
# l=list(map(int,input().split()))
# list=[]
# for i in range(len(l)):
#     ele=l.count(i)
#     print(ele)
#     # list.append(ele)
# # print(max(list))
n=int(input())
l=list(map(int,input().split()))
c=1
x=l.count(1)
for i in range(2,6):
    ele=l.count(i)
    if x<ele:
        c=i
        x=ele
print(c)


    


