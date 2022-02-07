#!/usr/bin/python3

import json

md = {'name': 'Dima', 'age': 16, 'gender': 'male'}

mds = json.dumps(md)

f = open('bd.json','w')
f.write(mds)
f.close()

f = open('bd.json','r')
result = f.read()
f.close()

print(json.loads(result)['name'])


print(mds)

# for item in md.items():
#     print(str(item[0])+'-'+str(item[1]))

# d1 = ['one', 'two', 'three']
# d2 = [1, 2, 3]


# mydict = dict(zip(d1,d2)) 

# dict2 = mydict.copy()

# print(dict2)

# print(mydict.get(3,'Nothing'))


# print('Done')