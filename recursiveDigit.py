    # superDigit(p) = superDigit(9875987598759875)
    #               9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    # superDigit(p) = superDigit(116)
    #               1+1+6 = 8
    # superDigit(p) = superDigit(8)


# while num>9:   
#     sum=0
#     while num!=0:
#         digit = num%10 
#         sum = digit+sum
#         num //=10
#     num = sum

# print(sum)  



# while num>9:
#     l = []
#     for i in str(num):
#         l.append(int(i))
#     p = sum(l)   
# print(p)



# p= input()
# k = int(input())
# n =p*k
# n = int(n)

# while n > 9:
#     num= sum(list(map(int,str(n))))

# print(num)

n,k=map(int,input().split())
p = int(str(n*k))
r= p%9
if r==0:
    print(9)
else:
    print(r)

