# def fun(m,n):
#     l=[]
#     for i in range(m,n):
#         if isPrime(i):
#             l.append(i)
#     return l

# check whether number prime or not         
# def isPrime(n):
#     for i in range(2,n//2):
#         if n%i==0:
#             return False
#     return True

# m=int(input())
# n= int(input())
# print(isPrime(n))
# print(fun(m,n))

def primefactor(n):
    for i in range(2,n+1):
        if n%i==0 and isPrime(i):
            print(i)

def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())

print(primefactor(n))




