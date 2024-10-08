'''
Created on 2024. 8. 12.

@author: user
'''
# Series : 1차원 배열같은 자료구조
# DataFrame : 2차원 배열같은 자료구조
#             행, 열의 개념이 있다(행, 칼럼)

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# [[][]]
arr = np.array([[1,2,3],[4,5,6]])
print('arr:',arr)
print(type(arr))
print(arr.ndim, arr.shape)
print(arr[1][2])
print()


df = pd.DataFrame(arr)
print('df:\n',df)
print(type(df))
print(df.ndim, df.shape)
print(df[2][1]) # df[칼럼명][인덱스이름]
print()

d = {'a':['1','3'] , 'b' :['1','2'] , 'c' : ['2','4'] }

df = pd.DataFrame(d)
print('df:\n',df)
print(df['a'][1])
print()

df = pd.DataFrame(data=[[4,5,6,7],[1,2,3,4]], 
                  index=range(0,2), 
                  columns=['A','B','C','D'])
print('df:\n',df)

s1 = pd.Series([10,40,30,20])
s2 = pd.Series(['A','B','C','D'])

df = pd.DataFrame([s1,s2])
print('df:\n',df)
print()


s1 = pd.Series(['서울', 2020, 1.5], index=['도시','year','pop'])
s2 = pd.Series(['서울', 2021, 1.7], index=['도시','year','pop'])
s3 = pd.Series(['서울', 2022, 3.6], index=['도시','year','pop'])
s4 = pd.Series(['부산', 2021, 2.4], index=['도시','year','pop'])
s5 = pd.Series(['부산', 2022, 2.9], index=['도시','year','pop'])

df = pd.DataFrame([s1, s2, s3, s4, s5], index=range(0,5))
print('df:\n', df)
print()