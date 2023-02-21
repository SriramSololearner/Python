n,k = map(int,input().split())
p = str(n)*k
sum =0
while p!=0:
    digit = p%10
    sum+=digit
    p = p//10
print(sum)