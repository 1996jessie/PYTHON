'''
Created on 2024. 8. 7.

@author: user
'''
import Ex02
s1 = Ex02.Student(10)
s1.info()

import Ex02 as ex
s1 = ex.Student(10)
s1.info()

from Ex02 import *
s1 = Student(10)
s1.info()