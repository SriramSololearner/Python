def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
l=[1,2,3,4,5,6]
print(list(map(fact,l)))