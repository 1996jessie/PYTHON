'''
Created on 2024. 8. 6.

@author: user
'''
# Ex04.py
# import 패키지.모듈
# import 패키지.모듈 as 별칭
# from 패키지.모듈 import 함수명1,함수명2 또는 *

import mypac.Ex01
print(mypac.Ex01.sum(3,5))
print(mypac.Ex01.sub(30,10))
print('----------------')

import mypac.Ex01 as ex
print(ex.sum(3,5))
print(ex.sub(30,10))

print('----------------')
from mypac.Ex01 import *
print(sum(3, 5))
print(sub(30, 10))
