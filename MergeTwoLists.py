l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
i=0
j=0
l.sort()
m.sort()
while i<len(l) and j<len(m):
    if l[i]<m[j]:
        k.append(l[i])
        i+=1
    else:
        k.append(m[j])
        j+=1
# k.extend(l[i:] or m[j:])
while i<len(l):
    k.append(l[i])
    i+=1
while j<len(m):
    k.append(m[j])
    j+=1
print(k)