# def fun():
#     print('Hello There')
# fun()
# fun()
# fun()

#returning multiple values
# def fun(a,b,c):
#     a=a*2
#     b=b+2
#     c=c-2
#     return a,b,c
# print(fun(3,5,6))

# once return statement in a function, function call will get terminated.
def sri():
    for i in range(10):
        print(i)
        return i

# l=[]
## l.append(l.append(5))
# l.append('srii')
# print(l)

# positional Arguments  based on actual parameters position
# def fun(a,b,c,d):
#     print(a,b,c,d)
# fun(6,5,3,4)  #based on actual parameters position

#keyword Arguments
# def fun(p,q,x,y):    #Based on the  formal parameters
#     print(x,p,y,q)
# fun(p=5,q=6,x=1,y=2)

#default parameter   # doesn't provided ANY VALUES default values be taken at function def
# def fun(a,b=3,c=2,d=9):
#     print(a,b,c,d)
# fun(5,8,4,8)

# variable length parameters
# def fun(*e):
#     print(e)
# fun(4,5,6,7,1,6,8,7)

#mutable objects passing as a arguments
# def fun(l):
#     l.append(6)
#     l.pop()
#     l[0]=5
#     l[1]=1
#     print(l)
# x=[1,2,3,4,5]
# fun(x)

#Immutable object passing as a arguments

# using global
# b=0           #global Scope Variable
# def fun():
#     global b
#     global a
#     a=400     # local scope variable
#     print(a)
#     print(b)

# fun ()  
# print(a)

# a=5
# def fun():
#     # global a
#     a=20
    
# print(a)
# fun()
# print(a)

# lambda Function
# lambda-- argument-- expresson
# x=lambda x,y:x-y
# print(x(18,10))

# x=lambda x,y:(x+2,y+5)
# print(x(7,9))
# x=lambda x:x*2
# print(x(5))

# map()   mapping asequence of elements
# l=[1,2,4,5,6,8]
# x=list(map(lambda x:x*x,l))
# print(x)

from functools import *
# Reduce  reduce into a single integer
l=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,l))
















