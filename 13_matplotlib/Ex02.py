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

plt.figure(figsize=(5,4))
plt.plot([1,2,3,4],[5,6,3,8],linewidth=8,alpha=0.5)
plt.xlabel('x축')
plt.ylabel('y축',rotation=0)
plt.title('matplotlib 예제')
plt.show()
