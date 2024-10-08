'''
Created on 2024. 8. 6.

@author: user
'''
# Ex05.py

import math
print(math.pi)
n = math.factorial(5)
print('n:',n)

from math import *

n = factorial(5)
print('n:',n)

from math import factorial as f
n = f(5)
print('n:',n)

def func(n):
    if n == 1:
        return 1
    return n * func(n - 1)
print(func(5))

print('-------------------')

n = sqrt(5)
print('n:',n)

print(max(4,2,7,5))
print(min(4,2,7,5))
print(abs(-3.7))
print(pow(2,3))
print(round(2.3))
print(round(2.7))
print(round(-2.3))
print(round(-2.7))
print(round(3.14568,3))
print(round(98513.14568,-3))

print('---------------------------')

import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())


from datetime import *

now = datetime.now()
print("now:" , now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(datetime.weekday(date(now.year,now.month,now.day)))
print(datetime.weekday(now))
# 월:0
# 화:1
# 일:6

def week(i) :
    days = ['월','화','수','목','금','토','일',]
    day = i.weekday()
    # print(days[i])
    print(days[day])

# week(datetime.weekday(now))
week(datetime.now())
    

    









