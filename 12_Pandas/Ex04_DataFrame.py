'''
Created on 2024. 8. 12.

@author: user
'''
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

idx = ['one', 'two', 'three', 'four']
col = ['서울', '부산', '광주', '대구']

df = DataFrame(np.arange(16).reshape((4,4)),
               index=idx,
               columns=col)

print('df:\n',df)
print()

print(df.reindex(index=['one','four']))
print()

print('df:\n',df)
print()

print(df.drop(index=['two','three']))
print()


df2 = df.reindex(columns=['부산','광주'])
print('df2:\n',df2)
print()

# df3 = df.drop(columns=['서울','대구'])
df3 = df.drop(['서울','대구'],axis=1)
print('df3:\n',df3)
print()

# one,three/부산, 광주
print(df.reindex(index=['one','three'], columns=['부산','광주']))
print()

print(df.drop(index=['two','four'], columns=['서울', '대구']))
print()

print(df.drop(['two','four'],axis=0).drop(['서울', '대구'],axis=1))
print()


print('-------------------------------------')

s = pd.Series(['A','B','C','D','E','F','G'], 
              index=[49,48,47,46 , 2, 3, 4])
print(s)
print(s[3])
print(s[47])
print(s.loc[3])
print(s.loc[47])
print(s.iloc[3])
# print(s.iloc[47])
print()
print(s.loc[:3])
print()

print(s.iloc[:3])
print()


print('df:\n',df)
print()

print(df.loc['two'])
print()
print(df.loc[['two']])
print()

print(df.loc[['two','three']])
print()

print(df.iloc[[1,2]])
print()

print('---------------------------------')


df = DataFrame([[-40, 70, 20], [50, -50, 20], [50, 20, 20]], \
                  columns=['국어', '영어', '수학'], 
                  index=['박보검', '홍길동', '아이유'])

print('df:\n',df)
print()

print(df.apply(np.max))# axis=0 
print()

print(df.apply(np.max,axis=1))
print()

print(df.apply(lambda x : x.max() - x.min(), axis=0))
print()
print(df.apply(lambda x : x.max() - x.min(), axis=1))
print()

mylambda = lambda x : x.max() - x.min()
print(df.apply(mylambda, axis=1))
print()

print('df:\n',df)
print()

print(df.sort_index())
print()

# print(df.sort_index(axis=1))
print(df.sort_index(axis='columns',ascending=False))
print()


print(df.sort_values(by='영어'))
print()


print(df.sort_values(by=['국어','영어'], ascending=[False,True]))
print()

print(df.apply(np.sum,axis=1))
print()
