# n = int(input('enter n value:'))
# x = int(input('enter x valaue'))
# sum=1
# fact=1
# for i in range(1,n+1):
#     fact = fact*i
#     y= x**i
#     sum = sum+(y//fact)
# print(sum)



# n = int(input())
# for i in str(n):
#     x= int(str(i)[::-1])   
# print(x)
# n = int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         break
# else:
#     for i in range(2,n):
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#     else:
#         print(j)

# x=min([2,0,3,1]) 
# y=not(x&0)
# z=y*2
# print(z)
# x=len(['b001']) #1
# y=list(range(x))#(0)
# z=y[-1]         #0
# print(z)        #0

# for number in 10,15:            # 10 15
#     for counter in range(1,3):  # 1 2 
#         print(number*counter,end=' ')
        # 10 20 15 30

a,b,c=9,6,6 
for c in range(5,10):  # 5                     6                          7                  8          9                    
    if (c+a)>(a-c):    #(5+9)>(9-5)=> 14>4 T   (6+17)>(17-6)=>23>11 T     33>19 T            40>24 T    48>30 T
        a=(b+c)+a      #a=(6+5)+9 =>11+9=20=a     a=11+17=>28               a=13+26=39         a=47        a=9+39=48 
        b=7&c          #b=7&5 =5                  b=7&6=6                   b=7&7=7            b=7&8=0     b=7&9=1
    a=a^c              #a=20^5=17              a=28^6=26                a=39^7=32          a=47^8=39     a=46
print(a+b) 

