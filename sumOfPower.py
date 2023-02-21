# n=str(int(input()))
# s=0
# for i in range(1,len(n)):
#     s=s+int(n[i-1])**int(n[i])
# print(s+1) 

# p,d,m,s=map(int,input().split())
# t=0

# k=n=0
# while t<=s:
#     if p>=m:
#         t=t+p
#         p=p-d
#         k=k+1
#     else:
#         t=t+m
#         k=k+1
# print(k-1)        
        
n=str(input())
l=list(map(int,list(n)))
s=1
for i in range(1,len(l)):
    s=s+l[i-1]**l[i]
print(s)









