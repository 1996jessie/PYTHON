'''
Created on 2024. 8. 2.

@author: user
'''
print('Ex02_input.py')
a = input('숫자 1 입력하세요: ')
b = input('숫자 2 입력하세요: ')
print(a + " 더하기 " + b + "은 " + str(int(a) + int(b)) + "입니다")
print("%d 더하기 %d은 %d입니다" % (int(a), int(b), int(a) + int(b)))

