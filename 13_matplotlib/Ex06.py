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

x1 = [1,2,3,4]
y1 = [3,7,6,4]
x2 = [1,2,3,4]
y2 = [4,6,8,5]

ymax = max(max(y1), max(y2)) + 1  # 7,8 => 9
ymin = min(min(y1), min(y2)) -1  # 3,4 => 2

plt.title('subplot 예제')
plt.subplot(2,1,1)
plt.plot(x1,y1,'yo-')
plt.ylabel('y1축')
plt.ylim(ymin,ymax)

plt.subplot(2,1,2)
plt.plot(x2,y2,'r.--')
plt.ylabel('y2축')
plt.ylim(ymin,ymax)

plt.show()
