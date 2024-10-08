'''
Created on 2024. 8. 6.

@author: user
'''
import os
print(os.getcwd())
print(os.listdir('.'))
print(len(os.listdir('.')))

def filetype(f):
    if os.path.isfile(f):
        print(f, ':File')
    elif os.path.isdir(f):
        print(f, ':Directory')
        

flist = os.listdir('.')
print('flist:', flist)

for fname in flist :
    # print(fname)
    filetype(fname)
print('---------------------')

# os.rename('test.txt','test2.txt') #FileNotFoundError

# os.remove('test3.txt')

# a\X
# b\b.txt

# os.rmdir('a')
# os.rmdir('b')

import shutil
# shutil.rmtree('b')

shutil.copy('test2.txt','test4.txt')













    