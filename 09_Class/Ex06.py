'''
Created on 2024. 8. 7.

@author: user
'''

class Person:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age
    def __str__(self):
        return '<Person %s %d>' % (self.name, self.age)
    
class Employee(Person):
    def __init__(self,name,age,position,salary):
        super().__init__(name, age)
        self.position = position
        self.salary = salary
        
    def __str__(self):  
        # return '<Employee %s %d %s %d>' % (self.name, self.age, self.position, self.salary)
        # return '%s - %s %d' % (super().__str__(), self.position, self.salary)
        return Person.__str__(self)+' '+self.position+' '+str(self.salary)
    
p1 = Person('제니', 30)
p2 = Person('조이')

print('p1 :', p1.__str__())
print('p2 :', p2)

e1 = Employee('태연', 40, '대리', 200)
e2 = Employee('수영', 50, '부장', 500)

print('e1 :', e1)
print('e2 :', e2)

# issubclass(자식,부모) //boolean
a = issubclass(Employee,Person)
print(a)

a = issubclass(Person,Employee)
print(a)
