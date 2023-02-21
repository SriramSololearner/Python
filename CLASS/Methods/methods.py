# instance method 
# class Rect:
#     def __init__(s,l,b):
#         s.l=l
#         s.b=b
#     def area(s):
#         print(s.l*s.b)
# ob = Rect(5,5)
# ob.area()


# Class Method
# class A:
#     #class Attributes
#     a=45
#     # b=5
#     def __init__(s,c):
#         # s.b=b
#         s.c=c
#     @ classmethod
#     def dip(cls):
#         print(A.b)
# ob=A(30)
# ob.b=55
# ob.dip()

class Rectangle:
    shape = "Rectangle"
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    @classmethod
    def get_shape(cls):
        return cls.shape

Rectangle.get_shape()
rect = Rectangle(5, 10)
print(rect.get_shape(4))



