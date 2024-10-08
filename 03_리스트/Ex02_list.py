'''
Created on 2024. 8. 5.

@author: user
'''
from conda.common._logic import TRUE
L = [10, 30, 40]
print('L : ', L)

L[1:1] = [20]
print('L : ', L)

L[4:]= [50]
print('L : ', L)

L.append(60)
print('L : ', L)

L.insert(2, 70)
print('L : ', L)

print()

i = 1
L2 = []
sum = 0
while True :
    i += 1;
    num = int(input('숫자 입력 : '))
    L2.append(num)
    sum += num
    if(i>5) :
        break
print('L2 : ', L2)
print('total : ', sum)

print()

l2 = []
total = 0
for i in range(5) :
    j = int(input('숫자 입력 : '))
    # l2[i:] = [j]
    l2 += [j]
    # l2.append(j)
    # l2.insert(i, j)
    
    total += j

print('l2: ', l2)
print('total: ', total)

print()

L3 = [30,20,10,70,20]
print('L3 : ', L3)
print(L3.index(20))
# print(L3.index(80)) #ValueError
# print(L3.count()) #TypeError
print(L3.count(20))
L3.remove(20)
# L3.remove(200) #ValueError
print('L3 : ', L3)
L3.reverse() #역순
print('L3 : ', L3)
L3.sort() #정렬(default : false)
print('L3 : ', L3)
L3.sort(reverse=TRUE) #내림차순 정렬
print('L3 : ', L3)

print()

L4 = ['banana', 'Grape', 'apple', 'orange']
print('L4 : ', L4)
L4.sort()
print('L4 : ', L4)

print()

L5 = ['123', '34', '56', '2345']
print('L5 : ', L5)
L5.sort()
print('L5 : ', L5)
L5.sort(key=int) #숫자로 생각해라
print('L5 : ', L5)