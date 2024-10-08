'''
Created on 2024. 8. 7.

@author: user
'''

class Student :
    name = "철수"
    
    def __init__(self, a):
        print('Student 생성자')
        
    def info(self):
        print("name :", self.name)

print(__name__)
if(__name__ == '__main__') : 
    s1 = Student(10)    
    s2 = Student(20)   
    
    s1.info()
    s2.info()