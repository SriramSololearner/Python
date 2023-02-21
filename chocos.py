# n,c,m = map(int,input().split())
# choc = n//c

#  # Initialize the number of chocolates with the amount of money
#     chocolates = n // c   
#     # Initialize the number of wrappers with the number of chocolates
#     wrappers = chocolates-
#     while wrappers >= m:
#         # Calculate the number of chocolates that can be exchanged
#         exchange = wrappers // m
#         # Add the number of exchanged chocolates to the total number of chocolates
#         chocolates += exchange
#         # Update the number of wrappers
#         wrappers = exchange + (wrappers % m)



t= int(input())
for i in range(t):
    n,c,m = map(int,input().split())    # 10 2 3             
    chocos = n//c                       #10//2 = 5
    wr = chocos                          #5 = 5 
    while wr>=m:                        #5>=3    true              3>=3 true       1>=3 false
        new_chocos=wr//m                #5//3 = 1                  3//3 = 1
        chocos+=new_chocos              #5+=1 = 6                   6+=1= 7
        wr = new_chocos+(wr%m)      #1+(5%3) =3                 1+(3%3) = 1 
    print(chocos)