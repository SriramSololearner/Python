# implicit 
# s='''hello
# wel
# come'''
# print(s)

# words = ['hello', 'world', 'python']
# result = ''
# for word in words:
#     result += word 
# print(result)
# Output: hello world python


# explicit
# s='helo wel \
# come to  \
# all '
# print(s)
# s=input()
# k=s[0:5]+s[5:].replace("s",)

# for i in range(1,20):
#     if 8**i==k:   
# k=input()                     #1221
# for i in range(len(k)//2):
#         if k[i]!=k[len(k)-1-i]:

#             print("No")
#             break
# else:
#     print('Yes')
# s=''' helo 
#  to
#  all 
# '''
# print(s)

# Accessing elements from given string

# str=input()
# for i in str:
#     print(i)
# slicing reverse

# s='welcome to python developers'
# print(s[::-1])

# reversing without slicing operations
# str=input()
# rev=''
# for i in str:
#     rev=i+rev
# print(rev)
# s='helolo to all'
# print(s.find('o'))
# print(s.rfind('o'))
     
# str='Hello all how are you'

# print(str[::-1])


# olleh all woh are uoy  output

str='Hello all how are you'
str=str.split()
#["hello","all",'how','are','you]
list=[]
for word in range(len(str)):
    if word%2==0:
        list.append(str[word][::-1])

    else:
         list.append(str[word])
print(list)

# s = 'Hello all how are you'
# output = ' '.join(word[::-1]  for word in s.split()) 

# s='qwertyuiopasdfghjklzxcvbnm '
# s=s.lower()
# s=s.replace(' ','')
# print(s)
# str=set(s)
# if len(str)==26:
#     print('Yes')
# else:
#     print('No')
s='helo to all'
print(s.partition('lpp'))

# s='TTTTTJJJJGGG'
# s=s.replace('T','Y')
# print(s)

# DNA='GCAT'

# "GCAT"  =>  "GCAU"

# str= ''.join(['U' if i=='T' else i for i in DNA])
# print(str)






