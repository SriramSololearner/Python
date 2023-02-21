# l=[[1,2,3],[2,3,4],[5,6,7]]
# for i in l:
#     print(*i)

# l=[]
# r=int(input())
# c=int(input())
# for i in range(r):
#     x=[]
#     for j in range(c):
#         x.append(int(input()))
#     l.append(x)

# print(l)

#Creating nestedList using append()

# l=[]
# r=int(input())
# for i in range(r):
#     x=[]
#     for i in range(r):
#         x.append(int(input()))
#     l.append(x)
# for i in l:
#     print(i)

# Creation of nestedList by using list comprehensions
# r=int(input())
# l=[[int(input()) for j in range(r)] for i in range(r)]
# print(l)
# for i in l:
#     print(*i)

# reading complete row in a single line

# n=int(input())
# l=[list(map(int,input().split())) for i in range(n)]
# print(l)

# addition of two matrices 

# r=int(input())
# c=int(input())
# l=[[int(input()) for j in range(c) ] for i in range(r)]
# print(l)
# m=[[int(input()) for j in range(c) ] for i in range(r)]
# print(m)
# r=[[x+y for i,j in zip(l,m) for x,y in zip(l,m)]]
# for i in r:
#     print(*i)

# orders=[]
# for i, order in enumerate(orders):
#     order.append(i+1)
#     orders.sort(key=lambda x: x[0] + x[1])
# print(order[2] for order in orders])
