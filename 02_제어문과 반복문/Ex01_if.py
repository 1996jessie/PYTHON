'''
Created on 2024. 8. 2.

@author: user
'''

su = 11

if su % 2 == 0 : 
    print('짝수')
    print('하하하')
else :
    print('홀수')
    print('호호호')
    
print('if~else 공부중')

print()

score = int(input('점수 입력하세요: '))

if score >= 90 :
    print('A학점')
elif score >= 80 : 
    print('B학점')
elif score >= 70 : 
    print('C학점')
elif score >= 60 : 
    print('D학점')
else :
    print('F학점')
    
print()

v = "pYtHon"
print(v)
print(v.upper())
print(v.lower())
print(v.isupper())

if v == "pYtHon" : 
    print("같다.")
else :
    print("같지 않다.")
    