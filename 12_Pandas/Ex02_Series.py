'''
Created on 2024. 8. 12.

@author: user
'''
import numpy as np
import pandas as pd
# from pandas import Series

arr = np.array([10,20,30,40])
print('arr:', arr)
print(type(arr))
print()

s = pd.Series([10,20,30,40])
print('s:', s)
print('type(s):',type(s))
print(s.ndim)
print(s.shape)
print(s.index)
print(s.values)
print(s[1])
# print(s[-1])
print()
print('--------------------')

s = pd.Series([10,40,30,20],index=['윤아','태연','제니','조이'])
print('s:', s)
print(s['태연'])
print(type(s['태연']))

print(s[['태연']])
print(type(s[['태연']]))
print()

s['조이']=100
s['아이유']=70
print('s:', s)
print()

print(s.index == '태연')
print(s[s.index == '태연'])
print()


print(s.values<50)
print(s[s.values<50])
print()
print('제니' in s)
print('슬기' in s)
print()

drops = s.drop(['태연','조이'])
print('drops:',drops)
print()
print('s:',s)
print()

print(s[1:3])
print()
print(s[3:1:-1])
print()
print(s[[1,3]])
print()
print(s['태연':'조이'])
print()
s[1:3] = 99
print('s:',s)
print()

print(np.max(s))
print(np.sum(s))
print()

s2 = s.sort_index(ascending=False)
print('s2:',s2)
print()

s2 = s.sort_values(ascending=False)
print('s2:',s2)
print()


