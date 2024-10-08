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

siljuk = [25,30,40,35,25,40]
members = ['윤아','수지','조이','정국','보검','동건']
colors = ['b','g','r','c','m','y']

for i in range(len(siljuk)) :
    # print(i) 0 1 2 3 4 5
    value = str(siljuk[i])+'건' # value='25건' '30건'
    plt.text(x=i, y=siljuk[i]+1,s=value) #(x=0,y=26/ x=1,y=31..)
  
plt.bar(members,siljuk,color=colors)
plt.xlabel('회원 이름')
plt.ylabel('회원 실적',rotation=0)
plt.title('회원별 업무 실적')

filename = 'barGraph02.png'
plt.savefig(filename)
plt.show()    