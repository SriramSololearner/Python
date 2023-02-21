# d = {1:10,2:20,3:30,4:40,5:50}
# for k,v in d.items():
#     print(k,v,sep=':')

d={'name':'ramu','age':25,'dept':'cse'}
d['marks']=45
d['name']='sri'
d.update({'id':2654})
d.update({'id':7865})
d.update({'name':'ramwsh'})

# accesing value using  key

# if 'names' in d:
#     print(d['names'])
# else:
#     print('not found')

# if 'age' in d:
#     print(d['age'])
# else:
#     print('not found')

print(d.get('modfd'))


