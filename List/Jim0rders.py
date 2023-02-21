# creation of nested lists
# l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l:
#     print(*i)

n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
list=[sum([x for x in i]) for i in l]
m=[]
for i,x in enumerate(list):
    m.append([i+1,x])
m.sort(key=lambda a:a[1])
print(m)
for i in m:
    print(i[0],end=' ')

# 5
# 8 1
# 4 2
# 5 6
# 3 1
# 4 3
# Customer	   1	2	3	4	5
# Order #		8	5	6	2	4
# Prep time  	3	6	2	3	3
# Calculate:
# Serve time	11	11	8	5	7
# 4 5 3 1 2
# 3 4 2 0 1

# [orders[i].append(i+1) for i in range(len(orders))]
#     orders = sorted(orders, key=lambda x: (x[0]+x[1],x[2]))
#     return [orders[i][2] for i in range(len(orders))]
    


