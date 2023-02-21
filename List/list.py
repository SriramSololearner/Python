# l =[1,8,5,'dfg',56.6]
# # accesing list of elements
# for i in l:
#     print(i)
# # we cannot modify the list
# for ele in range(len(l)):
#     print(l[ele])

# l = []
# n = int(input('enter n values:'))
# for i in range(n):
#     l.append(int(input('enter elele :')))
# print(*l)

#Adding elements dynamically

# n = int(input('enter n value:'))
# list = [None]*n
# print(list)
# for i in range(len(list)):
#     list[i] = int(input('enter ele'))
# print(*list).

# #########     using map function
# lst  = list(map(int,input().split()))
# print(lst)

####  list comprehension method 
# list = [int(i) for i in input().split()]
# list = []
# n = int(input())
# for i in range(n):
#     list.append(int(input()))
# print(*list)

# l=[1,23,5,6,3,6,5,6]
# print(min(l))
# print(max(l))
# l.insert(3,'tfgy')
# l.insert(5,'s5g')
# l.insert(5,'ty')
# print(l)
# l.pop()
# l.pop(1) 
# print(l.pop(5))
# l.remove(1)
# l.remove(6)
# print(l)




# l=[1,5,6,7,6,1,2,3,2,4,2,4,2]
# k=int(input()) 
# for i in range(len(l)):
#     if l[i]==k:
#         print(i)

# l=[int(i) for i in range(int(input()))]
# print(l)
# l=[int(input()) for i in range(int(input()))]
# print(l)

# l=[1,5,4,3,2,1,6,5,8,7,4,5,6,1,2,3,5,2,3]
# s=set(l)
# l=list(s)
# print(l)

#delet duplicate elements form list
# l=[1,5,4,3,2,1,6,5,8,7,4,5,6,1,2,3,5,2,3]
# x=[]
# for i in l:
#     if i not in x:
#         x.append(i)

# searching an elemet
# l=[1,5,4,3,2,1,6,5,8,7,4,5,6,1,2,3,5,2,3]
# k=int(input())
# x=[]
# for i in range(len(l)):
#     if l[i]==k:
#         x.append(i)
# print(x)

# to count the repetation of elememnts
# l=[1,5,4,3,2,1,6,5,8,7,4,5,6,1,2,3,5,2,3]
# k=int(input())
# c=0
# for i in range(len(l)):
#     if l[i]==k:
#         c+=1
# print(c)


# l=[1,2,3,4,5,2,3,2,5,4,23,6,5,6]
# k=int(input())
# x=l[:k]
# y=l[k:]
# x.sort()
# y.sort(reverse=True)
# print(x+y)

# n=int(input())
# l=list(map(int,input().split()))
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# # print(d)
# # print(sorted(d.items()))
# lst=sorted(list(d.items()),key=lambda x:x[0],reverse=True)
# print(lst)
# print(lst[0][0])

# l=list(map(int,input().split()))
# for i in range(len(l)):
#     if l[i]==0:
#        l.append(l.pop(i))

# l=list(map(int,input().split()))
# for i in range(len(l)):
#     x=l.count(0)
#     for i in range(x):
#         l.remove(0)
#         l.append(0)
# print(l)

# n=int(input())
# l=list(map(int,input().split()))
# # t=int(input())
# m=list(map(int,input().split()))
# lst=[]
# for i in m:
#     d={}
#     d[i]=d.get(i,0)+1
# print(d)
# lst=sorted(list(d))
# print(lst)
# print(lst[0][0])

# 10
# 203 204 205 206 207 208 203 204 205 206
# 13
# 203 204 204 205 206 207 205 208 203 206 205 206 204

    # 1 2 3 4 0 5 0 9 0 7

# def multiply(a, b):
#         return a*b
        
# a=int(input())
# b=int(input())
# print(multiply(a,b))

l=['10101','11100','11010','00101']

for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        print(l[i],l[j])



        







                                                                                                                                   