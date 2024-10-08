'''
Created on 2024. 8. 6.

@author: user
'''
def minus(a,b):
    return a-b

print(minus(20,9))
print(minus(a=20,b=9))
print(minus(b=9,a=20))
# print(minus(c=9,a=20))

def test(a,b=7,c=8):
    return a+b+c

print(test(10,20,30))
print(test(10,20))  
print(test(10)) 
print()


def test2(*args):
    print(args,"-", type(args))
    for i in args:
        print(i,'/',end=' ')
    print('--------')

test2(1,2)
test2(1,2,3,4,5)
test2()
test2([1,2,3],(4,5,6))
test2('orange','melon','apple')
    
print()

def func(n):
    if n==1:
        return 1
    return n + func(n-1)

print(func(10))









  