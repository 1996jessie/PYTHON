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

x1 = [1,2,3,4]
y1 = [3,7,6,4]
x2 = [1,2,3,4]
y2 = [4,6,8,5]

plt.plot(x1,y1,color='r',label="first line")
plt.plot(x2,y2,color='green',label="second line",linestyle='dotted', marker='D')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('Ex03 예제')
plt.legend()

plt.annotate('annotate',
             xy=(1.5,5),
             xytext=(2,4),
             arrowprops={'color':'green'})


filename = 'brokenLine01.png'
plt.savefig(filename)
plt.show()

