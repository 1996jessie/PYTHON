'''
Created on 2024. 8. 5.

@author: user
'''

t1 = () #tuple
t2 = (1, 2, 3) #tuple
t3 = 1, 2, 3 #tuple
t4 = (1,) #tuple
t5 = 1, #tuple
t6 = (1) #int
t7 = 1 #int

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
print(t6, type(t6))
print(t7, type(t7))

t = (1,2,3)
t2 = t + ('kim', 'park')
print('t2 : ',t2)

t2 = t, ('kim', 'park')
print('t2 : ',t2)
print('t2[1][0] : ',t2[1][0])
print('len(t2) : ',len(t2))

print()

x, y, z = 1, 2, 3
print('x, y, z :', x, y, z)
x,y = y,x
print('x, y, z :', x, y, z)

print()

t = (1, 2, 3)
x, y, z = t
print('x, y, z :', x, y, z)

L = list(t)
print('L :', L)
L[1] = 22
print('L :', L)
t = tuple(L)
print(t)
