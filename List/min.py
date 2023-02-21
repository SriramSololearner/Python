list = [int(i) for i in input('enter values :').split()]
mm = 10000
for i in list:
    if i<mm:
        mm=i
print(mm)