'''
Created on 2024. 8. 6.

@author: user
'''
# Ex03.py

import Ex01
Ex01.abc()
Ex01.xyz()

print('--------')
import Ex01 as e
e.abc()
e.xyz()
print('--------')

# from Ex01 import abc,xyz
from Ex01 import *
abc()
xyz()
print('###############')

import Ex02
Ex02.display()
print('--------')

import Ex02 as x 
x.display()
print('--------')

from Ex02 import *
display()
















