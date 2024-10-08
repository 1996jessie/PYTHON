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


# df:
#      국어  영어  수학
# 웬디  40  50  50
# 슬기  70  50  20
# 조이  20  20  20
idx = ['웬디','슬기','조이']
col = ['국어','영어','수학']

df = pd.DataFrame(data=[[40,50,50],[70,50,20],[20,20,20]],
                  index=idx,
                  columns=col)
print('df:\n', df)
print()

# df = pd.DataFrame({'국어':[40,70,20],'영어':[50,50,20],'수학':[50,20,20]},idx)
# print('df:\n', df)
# print()

# df.plot(kind='bar')
# df.plot.bar()
# df.plot.barh()
df.plot.barh(stacked=True)

plt.show()
