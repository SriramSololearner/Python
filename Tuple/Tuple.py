# t=(1,2,3,4,5)
# print(t[:3])
t=(1,5,6,7,8,9)
print(t.index(5))
t=t[:1]+(2,3)+t[1:]
print(t)
print(min(t))
print(max(t))
print(sum(t))
print(t.count(5))
print(len(t))
print(t.index(5))

for i in t:
    print(i,end=' ')