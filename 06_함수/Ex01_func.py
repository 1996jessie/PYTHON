'''
Created on 2024. 8. 6.

@author: user
'''

#
# public String setName(String n){
#        
# }

def add(a,b):
    print('add함수')
    print(a+b)
    return a+b

add(10,20)
print(add(3,4))
print(add(3.1,4.2)) 
print(add([1,2,3],[10,11,12]))

def simple():
    pass

print(simple())

def myabs(x):
    if x < 0 :
        x = -x
    return x


def addabs(a,b):
    c = add(a,b)
    return myabs(c)

print(addabs(-5,-7))


# print(myabs(-10))

# a=2
# switch(a){
#     case 1: syso(1);break;
#     case 2: syso(2);break;
#     default: syso(3);break;
# }

def test(x):
    return{
        'a' : 1,
        'b' : 2,        
    }.get(x,9)    

print(test('b'))
print(test('k'))














    







