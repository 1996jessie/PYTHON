'''
Created on 2024. 8. 8.

@author: user
'''

try : 
    a = int(input('숫자 입력 :'))
    b = int(input('숫자 입력 :'))
except ValueError as err :
    print('숫자로 입력하세요')
else :
    print(a + b)

# open('a.txt','r')
# 없으면 파일 발견 못함
# 있으면 파일의 내용을 읽어서 출력

try: 
    fr = open('a.txt', 'r',encoding='utf-8')
except FileNotFoundError as err:
    print('파일 발견 못함')
else:
    s = fr.read()
    print(s)
    fr.close()
finally:
    print('finally')


print('-----------')

try:
    a = int(input('숫자 입력 :'))
    b = int(input('숫자 입력 :'))
    if a<0 or b<0 :
        # 내가 예외를 발생
        raise ArithmeticError('음수 입력됨')
    
except ArithmeticError as e:
    print("예외 발생:",e)
else:
    print("두 수 모두 양수 입력됨")