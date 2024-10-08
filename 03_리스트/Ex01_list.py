'''
Created on 2024. 8. 5.

@author: user
'''

L = [10, 20, 30]
print('L :', L)
a=10
print(type(a))
print(type(L))
print(L[0])
print(L[1])
print(L[2])
#print(L[3]) //list index out of range
print(L[-0])
print(L[-1])
print(L[-2])
print(L[-3])
# print(L[0]) = print(L[-0]) = print(L[-3])
print()

print("len(L) : ", len(L))
print(L.__len__()) #길이 구하는 함수

for i in range(0, len(L)):
    print(L[i], end=" ") 

print()

print(30 in L)
print(70 in L)
print(L + L)
print(L * 3)

print()

print(L[1:2]) #[시작위치:끝위치] : 시작위치 ~ 끝위치-1
print(L[1:3])
print(L[1:5])
print(L[1:])
print(L[:2])
print(L[:])

L[1] = 222;
print('L :', L)

print()

L2 = [10,20,30,40,50,60,70,80]
print('L2 :', L2)
print(L2[1:3])
print(L2[1::3])
print(L2[0::2])
print(L2[::-2])

print()

L3 = ['apple', 'banana', 100, 200]
print('L3 :', L3)
print(L3[1])
L3[1:1] = [300] #1:1은 0과 1 사이에 끼워넣기
print('L3 :', L3)
L3[1:2] = [1,2,3,4,5] #1자리에 대체
print('L3 :', L3)
L3[2:3] = ['tomato'] 
print('L3 :', L3)

# L3[2:3] = 'tomato' #{'t','o','m','a','t','o']
# print('L3 :', L3)

L3[0:2] = []
print('L3 :', L3)
L3[4:] = [10]
print('L3 :', L3)

del(L3[2])
print('L3 :', L3)
del(L3)
#print('L3 :', L3) #NameError