# def insertion_sort(arr):

#     n = arr.length
#     for i in range(1,n):
#         key = arr[i]    # start from arr[1]
#         j = i - 1       # j is left element of pair of i
#         # as long as j is greater than or equals to 0 and left 
#         # element(arr[j]) of key is bigger than key, 
        
#         while j >= 0 and arr[j] > key:
#            # swap: its left item will move to key
#            arr[j + 1] = arr[j]
#            # j moves down to the left
#            j = j - 1
#         # once all sorted, move elements where j stopped lastly
#         arr[j + 1] = key

#     print(arr)

# l=[9,7,4,5,1,3]
# for i in range(1,(len(l))):
#     j=i-1
#     while j>=0 and l[i]<l[j]:
#         j=j-1

#     l.insert(j+1,l.pop(i))
# print(l)

# l=[1,2,3,8,6,8,9,5,78,5,4,6,5,2,6,8]
# x=[]
# for i in l:
#     if i not in x:
#         x.append(i)
# print(x)