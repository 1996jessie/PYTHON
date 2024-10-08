'''
Created on 2024. 8. 13.

@author: user
'''
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt

font_location='c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)

slices = [1,2,3,4]
hobby = ['공부','게임','영화감상','운동']
color = ['c','m','r','b']

plt.title('취미')
plt.pie(slices,labels=hobby, colors=color,
        startangle=90,shadow=True,
        explode=(0,0.2,0,0),
        autopct = '%1.2f%%')
plt.legend(loc=1)
plt.show()

