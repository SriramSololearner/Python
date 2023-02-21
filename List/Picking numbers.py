a=[4,6,5,3,3,1]
c=0
l=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j]-a[i]<=1:
            c+=1
            l.append(a[j])
        else:
            break
print(max(l))

# max_count = 0
# for i in range(len(a)):
#     count = 0
#     for j in range(i, len(a)):
#         if a[j] - a[i] <= 1:
#             count += 1
#         else:
#             break
#     max_count = max(max_count, count)
#     print(max_count)
