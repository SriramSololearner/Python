n=int(input())
if (n%400==0) or (n%4==0 and n%100!=0):
    print('it is leap Year')
else:
    print('Not a leap year')
 