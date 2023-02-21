a1 = int(input())
v1 = int(input())
a2 = int(input())
v2 = int(input())

while (a1>a2 and v1>v2) or (a2>a1 and v2>v2):
    if a1+v1 == a2+v2:
        print('YES')
    else:
        a1 += v1
        a2 += v2
print('NO')

