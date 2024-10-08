'''
Created on 2024. 8. 7.

@author: user
'''
class Person :
    lastname = '김'
    def __init__(self):
        print('Person 생성자')
    def setname(self, name):
        print('self :', self)
        self.fullname = self.lastname + name
        print('fullname :', self.fullname)
        
p1 = Person()
p2 = Person()

print('p1 :', p1)
print('p2 :', p2)

print(p1.lastname)
print(p2.lastname)
print(Person.lastname)

p1.setname('연아')
p1.setname('보검')
