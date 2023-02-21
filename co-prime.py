a=int(input())
b=int(input())
while True:
    r=a%b
    if r==0:
        if b==1:
            print('it is A COPRIME')
        else:
            print('not a coPrime')
        break
    
    a=b
    b=r

    