'''
Created on 2024. 8. 5.

@author: user
'''

i = 1
while i < 5 :
    print(i)
    i += 1
print('while문 끝')

print()

i = 1
while True :
    print(i)
    i += 1;
    if(i>5) :
        break
print('while문 끝')

print()

sum = 0
count = 0

while True:
    score = int(input('점수 입력 : '))
    if score < 0:
        break
    count += 1
    sum += score
    
print('반복횟수 :', count)
print('합계 : ', sum)
print('평균 : ', sum/count)

print()

