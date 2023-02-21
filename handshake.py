t = int(input())
for i in range(t):
    n = int(input())
    x=0
    for i in range(n,-1,-1):
        if i==0:
            print(x)  #i=3        i=2    i=1
        else:
            x=x+(i-1)  # x= 2     2+1=3   3 




# n = int(input('enter n value:'))   
# print((n*(n-1)//2))
