'''
Created on 2024. 8. 7.

@author: user
'''



class Bank :
    rate = 0.3
    def __init__(self, m):
        self.m = m
    def save(self):
        self.m = self.m * (1 + Bank.rate)
    def show(self):
        print(int(self.m))

b1 = Bank(10000)
b2 = Bank(30000)

b1.save()
b2.save()

b1.show()
b2.show()