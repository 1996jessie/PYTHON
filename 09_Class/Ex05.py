'''
Created on 2024. 8. 7.

@author: user
'''

class Super:
    def __init__(self):
        print('Super init')
    def show(self):
        print('Super show') 
           
class Sub:
    def __init__(self):
        Super.__init__(self)
        # super().__init__()
        print('Sub init')   
    def show(self):
        print('Sub show') 

class Sub1(Super): # class 자식클래스 extends 부모클래스 => class 자식클래스(부모클래스)
    def __init__(self):
        # Super.__init__(self)
        super().__init__()
        print('Sub1 init') 
        
    # def __init__(self):
    #    super().__init__()
            
    def show(self):
        # Super.show(self)
        super().show()
        print('Sub1 show')     

sp = Super()
print('----------')
sb = Sub()
print('----------')
sb1 = Sub1()
sb1.show()
print('----------')