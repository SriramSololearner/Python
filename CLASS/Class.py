#creation of class
# class A:
#     def method(self):
#         print('hello')
# ob=A()
# ob.method()

# initialization of Variables

# class A:
#     def __init__(self):
#         self.a=20
#         self.b=30
#     def disp(s):
#         print(s.a,s.b,end=' ')

# ob=A()
# ob.disp()

# dynamically Creating varaibles

# class A:
#     y=20
#     def __init__(s,a):
#         s.x=a
#     def disp(s):
#       print(s.x,s.b)


# ob=A(25)
# ob.b=45
# print(ob.x,ob.y)
# ob.disp()

# instance varaibles 
# class Variables are shared AMONG all instances of class

class person:
    prof='busine'
    def __init__(s,name,age):
        s.a=name
        s.b=age
    def fun(s):
        print(s.a,s.b,person.prof)
ob=person('ram',25)
ob.fun()
pr=person('raju',46)
pr.fun()











        



