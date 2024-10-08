'''
Created on 2024. 8. 2.

@author: user
'''
#
# for 변수 in 반복할 데이터 : 
#     반복할 문장1
#     반복할 문장2
#
# 반복할 데이터
# range(시작, 끝, 증가값) ( 끝-1까지 )
# range(시작, 끝) (1씩 증가)
# range(끝) (0부터)

for i in range(1, 10, 3) : 
    print(i)

print()
  
for i in range(1, 10) : 
    print(i)    

print()
   
for i in range(10) : 
    print(i)    
    
print()

sum = 0

for i in range(1, 10, 3) : 
    sum += i
print(sum)

print()

oddSum = 0
evenSum = 0
for i in range(1, 11) :
    if i % 2 == 1 :
        oddSum += i
    else :
        evenSum += i
print("홀수의 합 :" , oddSum)
print("짝수의 합 :" , evenSum)