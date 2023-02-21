# n=int(input())
# l=[]
# for i in range(n):
#     l.append([input(),eval(input())])
# x=sorted(l, key=lambda x:(x[1],x[0]))
# x=[['Tina', 37.2], ['Berry', 37.21], ['Harry', 37.21], ['Harsh', 39], ['Akriti', 41]]
# grd=[]

n = int(input())
l=[]
grds=[]
for i in range(n):
    name=input()
    grade=eval(input())
    l.append([name,grade])
    grds.append(grade)
grds=list(set(grds))
grds.sort()
# secondLow=grds[1]

names=[]
for i in l:
    if i[1]==grds[1]:
        names.append(i[0])

names.sort()
for i in names:
    print(i)

# print(grds)
# print(l)

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39



