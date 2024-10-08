'''
Created on 2024. 8. 6.

@author: user
'''

dan = 3
for i in range(1, 10):
    # print(3, '*', i, '=', dan*i)
    print("3 * %d = %d" % (i, 3*i))
print()
print('----------------------------')

# gugudan.txt w
f = open('gugudan.txt','w')
for i in range(1, 10):
    f.write("3 * %d = %d\n" % (i, 3*i))
f.close()

print('gugudan.txt에서 read() 읽어서 console창에 출력하기')
f = open('gugudan.txt','r')
str = f.read()
print('str:',str)
print(type(str))
f.close()


print('gugudan.txt에서 readline() 읽어서 console창에 출력하기')
f = open('gugudan.txt','r')
while True:
    str = f.readline()
    print(str,end='')
    if str == '':
        break
    
print(type(str))
f.close()


print('gugudan.txt에서 readlines() 읽어서 console창에 출력하기')
f = open('gugudan.txt','r')
# str = f.readlines()
# ['','','']
for line in f.readlines() :
    print(line,end='')
    
# print('str:', str)    
# print(type(str))
f.close()

# read():
# readline():
# readlines():








