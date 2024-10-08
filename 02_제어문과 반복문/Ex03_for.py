'''
Created on 2024. 8. 5.

@author: user
'''

for i in range(1, 6) : 
    for j in range(7, 9) :
        print(i, j)
    print('---')
print('###')

print() 

print('for 구구단 시작')
for i in range(2, 10) :
    print('***', i, '단', '***')
    for j in range(1, 10) :
        print(i, '*', j, '=', i*j)
    print('-----------')
print('구구단 끝')    

print()

for i in range(1, 6, 1) :
    if (i == 2) :
        continue;
        print(i, end=' ')
    else : 
        print(i, 'else block')        
print()

for i in range(1, 6, 1) :
    if (i == 2) :
        break;
        print(i, end=' ')
    else : 
        print(i, 'else block')        
print()