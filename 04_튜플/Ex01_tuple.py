'''
Created on 2024. 8. 5.

@author: user
'''

L = [1,2,3,4,5]
print('L :', L)
print('type(L) :', type(L))

t = (1,2,3,4,5) #변경 불가능
print('t :', t)
print('type(t) :', type(t))

print('t[0] :', t[0])
print('t[-1] :', t[-1])
print('len(t) :', len(t))
print('len(t) :', t[0:2])
print('len(t) :', t[2:])
print('t[:2] :', t[:2])
print('t[::2] :', t[::2])

for i in range(len(t)) :
    print(t[i], end=' ')
print()
for i in t :
    print(i, end=' ')

print(t * 3)
print(3 in t)