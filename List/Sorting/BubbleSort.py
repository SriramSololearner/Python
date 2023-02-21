l=[1,5,4,3,2,1,6,5,8,7,4,5,6,1,2,3,5,2,3]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            l[i],l[j]=l[j],l[i]
print(l)
