# t= int(input())
# for i in range(t):
#     a,b = map(int,input().split())
#     c=0
#     for i in range(a,b+1):    #3,9
#         for j in range(1,i+1):     #1,2,3
#             if j*j==i: 
#                     c+=1
#                     break
#     print(c)  
import math

a,b = map(int,input().split())
n = int(math.ceil(math.sqrt(b)-math.floor(math.sqrt(a))))
print(n)  



