'''
Created on 2024. 8. 12.

@author: user
'''

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']

filename = 'capital_area.csv'
df = pd.read_table(filename,sep='|', header=None, names=mycolumn)
print("df:\n", df)
print(type(df))
print()

print(df['영업소코드'])
print()
print(df[['영업소코드']])
print()

print(df.reindex(columns = ['영업소코드']))
print()

print(df[['영업소코드', '총교통량', '1종교통량']])
print()

print(df.reindex(columns = ['영업소코드', '총교통량', '1종교통량']))
print()

print('영업소 코드별로 그룹')
dfgroup = df.groupby('영업소코드')
print('dfgroup:\n', dfgroup)
print()

result = dfgroup.sum()
print('result:\n', result)
print()
result_len = dfgroup.__len__()
print('result_len:\n', result_len)
print('result_len:\n', len(dfgroup))
print()

result = dfgroup['총교통량'].sum()
print('result:\n', result)
print()

result = df.groupby('영업소코드')['총교통량'].sum()
print('result:\n', result)
print()

# 영업소 코드별로 그룹묶어 2종 교통량, 총교통량의 합계 구하기

result = df.groupby('영업소코드')[['2종교통량', '총교통량']].sum()
print(result)
print()

result = df.groupby('영업소코드')[['2종교통량', '총교통량']].apply(np.sum)
print(result)
print()

print('영업소코드 190')
print(df['영업소코드'])
print()


print(df[df['영업소코드'] == 190])

print(len(df[df['영업소코드'].values==190]))
print(df[df['영업소코드'] == 190].__len__())
print()

# 1종교통량의 가장큰값, 가장작은값 출력
print(df['1종교통량'].max(),df['1종교통량'].min() )


# 영업소코드별로 그룹묶어 각 영업소 1종교통량 가장 큰값
print(df.groupby('영업소코드')[['1종교통량']].max())

print('--------------------------------------')

# 집계일자 별로 그룹묶어 총교통량 평균
result = df.groupby('집계일자')['총교통량'].mean()
print(result)
print()

# 집계일자 별로 그룹묶어 총교통량 평균이 1300이상인 데이터만 출력

print(df.groupby('집계일자')['총교통량'].mean()[df.groupby('집계일자')['총교통량'].mean() >= 1300])
print()

print(result >=1300)
print()
print(result[result >=1300])
print()

result = df.groupby(['집계일자','집계시'])['총교통량'].sum()
print(result)
print()
print('---------------------------------------------')

mycolumn = ['영화명','극장','지역','관람등급']

# 1.
filename = 'theater.csv'
df = pd.read_csv(filename, sep=',', header=None, names=mycolumn, encoding='euc-kr')
print("df:\n",df)
print()

print(df.groupby('극장')['영화명'].count())
print()



print(df.groupby(['영화명','지역'])['영화명'].count())
print()



