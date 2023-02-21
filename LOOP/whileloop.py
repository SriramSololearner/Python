# n = int(input())
# i=2
# while i<n:
#     if n%i==0:
#         print('it is not A prime number')
#         break
#     i=i+1
# else:
#     print('it is prime')

# n = int(input())
# sum=0
# i=1
# while i<n:
#     if n%i==0:
#         sum=sum+i

#     i=i+1
# if sum==n:
#     print('perfect')
# elif sum>n:
#     print("Abundant number")
# else:
#     print('defficient ')

# sum of Individual numbers
# n = int(input())
# s=0
# for num in str(n):
#     s = s+int(num)
# print(s)

# n = int(input())
# s=0
# while n!=0:
#     s+=n%10
#     n//=10
# print(s)

# rev
# n = int(input())    #4554
# rev=0
# n_copy=n
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit                                      
#     n=n//10
# if n_copy==rev:
#     print('palindrome')
# else:
#     print('not p')

#lucky or not 7 or 9

# n = int(input())
# while n!=0:
#     d=n%10
#     if d==7 or d==8:
#         print('it is a lucky')
#         break
#     n=n//10
# else:
#     print('not a lucky number')  

# 2 -1  0 count the pos and neg count numbers

# pos= neg= 0
# while True:
#     n = int(input())
#     if n>0:
#         pos+=1
#     elif n<0:
#         neg+=1
#     else:
#         print(pos)
#         print(neg)
#         break

# count the repeated digit in the number
# n = int(input())
# k = int(input())
# c=0
# while n!=0:
#     d= n%10
#     if d==k:
#         c+=1
#     n//=10
# print(c)


# n=int(input())
# k=n%10
# while n!=0:
#     d=n%10
#     if d>k:
#         k=d
#     n=n//10
# print(k)

# n = int(input())
# r=n%9
# if r==0:
#     print(9)
# else:
#     print(r)
    
#sum of digits until single digit
# n = int(input())
# while n>9:
#     s=0
#     while n!=0:
#         d=n%10
#         s=s+d
#         n=n//10
#     n=s
# print(s)

# n = int(input())
# m=int(input())
# while True:
#     for i in range(m,n//2+1):
#         if n%i==0:
#             n+=1
#             break
#     else:
#         x=n
#         rev=0
#         while x!=0:
#             d=x%10
#             rev=rev*10+d
#             x=x//10
#         if n==rev:
#             print(rev)
#             break
#         n=n+1

# narest program
n = int(input())

while True:
    for i in range(2,n//2+1):
        if n%i==0:
            n=n+1
            break
    else:
        print(n)
        break








