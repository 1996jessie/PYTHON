'''
Created on 2024. 8. 8.

@author: user
'''
class NumBox:
    def __init__(self,num): #num:40, self:100번지
        self.num = num
        self.num2 = num
        
    def __add__(self,num):
        self.num += num
        return '더하기' + str(self.num)
    
    def __sub__(self,num):
        self.num -= num
        return '빼기' + str(self.num)
    
    def __radd__(self,num):
        self.num += num
        return 'r더하기' + str(self.num)
        
print(1+2)
print("1"+"2")
print(1+int("2"))
print("1"+str(2))

print('----------')

num = NumBox(40) #num:100번지
print(num.num)
print(num.num2)
print(num.num + 50)
print(num + 50) # 객체+숫자
print(num - 50) # 객체-숫자

print(3 + num)# 숫자+객체

# 메서드 overloading : 
# 같은 클래스 내에서 메서드명은 동일하지만 매개변수 유형(타입, 갯수)이 다른것을 여러개 정의하는 것
# 메서드 overriding : 
# 자식클래스가 부모클래스로부터 상속받은 메서드를 재정의(유형(타입, 갯수)이 같아야 한다.)

# 연산자 오버로딩

