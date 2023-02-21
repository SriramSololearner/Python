n =int(input('enter n value:'))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum == n:
    print('Perfect number')
elif sum>n:
    print('Abundant Number')
else:
    print('deficient number')