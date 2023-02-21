# clock wise
# list = [int(i) for i in input().split()]
# k=int(input())
# k = k%(len(list))
# print(list)
# for i in range(k): #012
#     list.insert(0,list.pop())    # 0th index deleting last element
#     print(list)

# anti-clockWise

# list=[2,3,6,5,4,8]
# k = 3
# for i in range(k):
#     list.append(list.pop(0))
#     print(list)

l=[2,5,8,7,6,9,3]    # [ 7,6,9,3,2,5,8 ] [6,9,3,2,5,8,7]
k=200
for i in range(k):
    l.insert(0,l.pop())
print(l)




