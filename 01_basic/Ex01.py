'''
Created on 2024. 8. 2.

@author: user
'''

print('abc')
print("가나다")
print(3)
print()
print('오늘은' + "즐거운" + '금요일' + "입니다.")
print('오늘은', "즐거운", '금요일', "입니다.")
print('오늘은'"즐거운"'금요일'"입니다.")
print('오늘은', "즐거운", '금요일', "입니다.", sep="~")
print()
print(34+56)
print("34"+"56")
print("34"+str(56))
print(34+int("56"))
print("*" * 3)
print("%d / %d = %d" %(10, 3, 10/3))
print("%d / %d = %f" %(10, 3, 10/3))
print("%d / %d = %.2f" %(10, 3, 10/3))
print(15/6)
print(15//6) 
print(15%6)
print("%d" % (15/6))
print(divmod(15,6))

a = 2
b = 3
a = a ** b
print("a :", a)
print((a > 0) and (a < b))
print((a > 0) or (a < b))
print( not((a > 0) or (a < b)) )

