'''
Created on 2024. 8. 13.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

font_location='c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

# 영업소코드별로 그룹묶어 1종~6종 합계구하기
#
# df:
#           1종교통량   2종교통량   3종교통량   4종교통량   5종교통량   6종교통량
# 영업소코드                                                 
# 101    4737462  161326  521368  101514   58810  236974
# 190    3017117  150361  201848  109270   72139  150397
# 253    4382687  163125  147206  140583  142128  259845
# 254    2121138   87445   96231   74986  154777  140641
# 651    1489378   33402   62096   15789   23098   91917
# 685    1116379   67311  103311   67228  159362   67398


mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', 
            'TCS하이패스구분코드', '1종교통량', '2종교통량', 
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량', 'Noname']

filename = 'capital_area.csv'
df = pd.read_table(filename, sep="|", header=None, names=mycolumn)


result = df.groupby('영업소코드')[['2종교통량','3종교통량','4종교통량','5종교통량','6종교통량']].sum()
print(result)
print()


result.plot.bar()
plt.title('교통량 평균')
plt.ylabel('교통량', rotation=0)
plt.xticks(rotation=0) #x축 글자 회전

plt.show()

