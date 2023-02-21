# n = int(input('enter n value:'))
# for i in range(1,n):
#     print(i) 

# n = int(input('enter n value:'))    4                  0 0   1 0  2 0  3 0
# for i in range(1,n): 0 1 2 3 4                           0 1   1 1  2 1  3 1                
#     for j in range(1,n): 0 1 2 3 4                       0 2   1 2  2 2  3 2       
#         print(i,j)                                     0 3   1 3  2 3  3 3

                                                        #  j  

# n = int(input('enter n value:'))                      # n = 5   1 2 3 4  
# for i in range(1,n):                                   j         
#     for j in range(1,n):                        i=1    1 2 3 4         
#         print(j,end=' ')                        i=2    1 2 3 4                                           
#     print()                                     i=3    1 2 3 4                                                                 
#                                                 i=4    1 2 3 4                                                                                                


# n = int(input('enter n value:'))            
# for i in range(1,n):                                       
#     for j in range(1,n):                     
#         print(i,end=' ')                    
#     print() 
#                                                                  
# n = int(input('enter n value:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
                                                                
#                                                                                                                
# n = int(input('enter n value:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#



# n = int(input('enter n value:'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('#',end=" ")
#     print()




# n = int(input('enter n value:'))
# for i in range(1,n+1):
#     for j in range(1,i-1,-1):
#         print(j,end=' ')

# n = int(input())
# c=0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or  i==j or i==n or j==1 or j==n or i==i-1 or j==j-1:
#             print('3',end=' ')
#         else:
#             print(i,end='')
    
#     print()

# n = int(input('enter n value n:'))
# c= int(input('enter c value:'))
# for i in range(n):
#     for j in range(c):
#         if (i==0 or i==n-1) or (j==0 or j==c-1):
#             print("%3d"%(3),end=' ')
#         else:
#             print("%3d"%(i),end=' ')
#     print()