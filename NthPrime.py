# python script for displaying nth prime number

# 
n = int(input())
prime=[2]

i=3
while len(prime)<n:
    for j in prime:
        if i%j==0:
            break
    else:
        prime.append(i)
    i+=1
print(prime)

