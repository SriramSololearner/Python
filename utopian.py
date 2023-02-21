# t = int(input())
# x=1
# for i in range(t+1):
#     if i%2==0:
#         print(x)
#         x=x+1
#     else:
#         x=x*2
# print(x)
#Sample Input

# 3
# 0
# 1
# 4

# Sample Output

# 1
# 2
# 7

# t = int(input())
# h=1
# for i in range(t):
#     x = int(input())
#     for i in range(x):
#         if i%2==0:
#             h*=2
#         else:
#             h+=1
#     print(h)


# n = int(input())
# l = list(map(int,input().split()))
# for i in range(len(l)):
#     x = l[i]
#     h=1
#     for i in range(x):
#         if i%2==0:
#             h*=2
#         else:
#             h+=1
#     print(h)


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
# print(l)
for i in range(len(l)):
    x = l[i]
    h=1
    for i in range(x):
        if i%2==0:
            h*=2
        else:
            h+=1
    print(h)