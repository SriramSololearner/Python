a=list(map(int,input().split()))
j = 0
i = 0
while i < len(a) - 1:
    j += 1
    if i + 2 < len(a) and a[i + 2] == 0:
        i += 1
    i += 1
print(j)