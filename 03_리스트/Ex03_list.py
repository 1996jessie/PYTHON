'''
Created on 2024. 8. 5.

@author: user
'''

a = [10,20,30]

for i in range(0, a.__len__()) :
    print(a[i], end = ' ')
print()
for i in a :
    print(i, end = ' ')

print()

L = [['kim', 'park'], [10, 20, 30]]
print('L :', L)
print('L[0] :', L[0])
print('L[1] :', L[1])
print('L[0][0] :', L[0][0])
# print('L[0][2] : ', L[0][2]) #IndexError
print('L[1][2] :', L[1][2])

print('len(L) :', len(L)) #행의 개수
print('len(L[0]) :', len(L[0]))
print('len(L[1]) :', len(L[1]))

print()

for i in range(0, len(L)) :
    for j in range(0, len(L[i])) : 
        print(L[i][j], end=' ')
    print()
print()
    
for x in L :
    for y in x :
        print(y, end=' ')
    print()
print()

i = 0
while i < len(L):
    j = 0
    while j < len(L[i]):
        print(L[i][j], end=' ')
        j += 1
    print()
    i += 1
print()

L2 = [ i for i in range(10) ]
print('L2 :', L2)

print()

a = [1,2,3]
b = ['x', 'y']
L3 = [[i,j]
        for i in a
            for j in b
     ]
print('L3 :', L3)

print()

jumsu = [90, 25, 40, 87, 52]
print('합계 :', sum(jumsu))
print('최대 :', max(jumsu))
print('최소 :', min(jumsu))

for a in enumerate(jumsu) :
    print(a)
    
for a, b in enumerate(jumsu) :
    print(a, '/', b)