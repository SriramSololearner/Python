# def stones(n, a, b):
#     s=set()
#     # Write your code here
#     for i in range(n):
#         s.add(a*(n-1-i)+b*i)


#     return sorted(*s)

# print(stones(4,10,100))
# n,a,b=map(int,input().split())
# l=[]
# l.append(a)
# l.append(b)
# print(l)
# m=[]
# for i in l:   
#     for j in l:
#         x=i+j
#         m.append(x)
# print(set(m))

l=list(map(int,input().split()))
m=[]
for i in range(len(l)):
    if l.count(l[i])==2:
        if l[i] in l[i+1:]:
            t=l.index(l[i],i+1)
            k=t-i
            m.append(k)
if len(m)==0:
    print(-1)     
else:
    print(min(m))           



