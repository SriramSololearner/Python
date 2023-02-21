# decorator is taking input as a funtion and it adds new funtionality and returns the updated funtion
def qub(sqr):
    def fun2(x):
        return x*sqr(x)
    return fun2

@ qub
def sqr(x):
    return  x*x 
print(sqr(5))