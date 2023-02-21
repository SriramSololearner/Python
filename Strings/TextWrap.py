s='ABCDEFGHIJKLIMNOQRSTUVWXYZ'

# print('ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ')
w=4
x=[]
for i in range(0,len(s),w):
    x.append(s[i:i+w])
print(x)

print("\n".join(x))




