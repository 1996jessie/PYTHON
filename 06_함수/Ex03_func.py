'''
Created on 2024. 8. 6.

@author: user
'''
x = 10

def func():
    # global x 
    # print('x1:',x)
    x=30
    x=x+3
    print('x1:',x)

func()
print('x2:',x)

def func2():
    print('x3:',x)

func2()

print('------------------------------')

# lambda 매개변수1,매개변수2 : 리턴값

a = lambda x : x**2
print(a(8))

#
# def a(x):
#     return x**2
# print(a(8))

b = lambda x,y : x+y 
print(b(10,20))












