n =int(input())
i=2
while i<n:
    if n%i==0:
        print('not Prime')
        break
    i=i+1
else:
    print('prime Number')


