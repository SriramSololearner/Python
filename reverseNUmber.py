# reverse number  
# 9213   3129
n= int(input())
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d  
    n//=10
print(rev)



