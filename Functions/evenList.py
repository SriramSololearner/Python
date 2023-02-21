# def even(n):
#     if n%2==0:
#         return True
#     return False
# n=int(input())
# l=[]
# for i in range(1,n+1):
#     if not(even(i)):
#         l.append(i)
# print(l)

# alternative even numbers
def even(n):
    l=[]
    for i in range(1,n+1):
        if i%2==0 and i%4!=0:
            l.append(i)
    return l
n=int(input())
print(even(n))