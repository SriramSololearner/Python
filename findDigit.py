n =input()                          #1012
count = 0                                  #0
for digit in (n):                       #str(1012) => 1   0
    if digit!='0' and int(n)%int(digit)==0:             # "0"!='0"  and  1012%1 ==0
        count+=1                                  #c=0+1=1
print(count)

