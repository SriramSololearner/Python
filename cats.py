# x=2  1
# y=5
# z=4           2        1
#          x         z      y
# 
#         catA = x-z  catB = y-z
#         catA > Catb :  CatA
#         catB>catA   :  catB
#         mouse C

x,y,z = map(int,input().split())
catA = abs(x-z)             #1-3 = -2      2-4=2
catB = abs(y-z)              # 2-3 = 1      5-4 =1
if catA>catB:
    print('Cat B')
elif catB>catA:
    print('Cat A')
else:
    print('Mouse C')