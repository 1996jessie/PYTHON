'''
Created on 2024. 8. 6.

@author: user
'''
f = open('test.txt','w')
f.write('applebanana\n')
# f.write('\n')
f.write('orange')
f.close()

# w : X=>생성, O:새로 생성
# a : X=>생성, O:뒤에 계속 추가

f = open('test.txt') # ,'r' default값
pos = f.tell()
print('pos:', pos)
a = f.read()
print('a:', a)
pos = f.tell()
print('pos:', pos)
f.seek(2)
pos = f.tell()
print('seek 후에 pos:', pos)
a = f.read()
print('a:', a)
f.close()








