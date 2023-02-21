# l = list(map(int,input().split()))
# even = [l[i] for i in range(len(l)) if l[i]%2==0]
# odd = [l[i] for i in range(len(l)) if l[i]%2==1]
# for i in range(len(even)):
#     for j in range(i+1,len(even)):
#         if even[i]>even[j]:
#             even[i],even[j]=even[j],even[i]
# print(even)
# for i in range(len(odd)):
#     for j in range(i+1,len(odd)):
#         if odd[i]<odd[j]:
#             odd[i],odd[j]=odd[j],odd[i]
# print(odd)
# m = []
# for i in range(len(even)):
#     m.append(even[i])
#     m.append(odd[i])
# print(m)

# l=[8,5,9,4,6,3,1,2,12,11]
# even=[l[i] for i in range(len(l)) if i%2==0]

# odd=[l[i] for i in range(len(l)) if i%2!=0]

# even.sort()
# odd.sort(reverse=True)
# print(even)
# print(odd)
# m=[]
# for i in range(len(even)):
#     m.append(even[i])
#     m.append(odd[i])
# print(m)

l=[8,5,9,4,6,3,1,2,12,11]
e=l[::2]
o=l[1::2]
e.sort()
o.sort(reverse=True)
print(e)
print(o)
m=[]
for i in range(len(e)):
    m.append(e[i])
    m.append(o[i])
print(m)