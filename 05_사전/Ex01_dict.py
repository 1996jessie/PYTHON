'''
Created on 2024. 8. 5.

@author: user
'''

d = {'one':'hana', 'two':'dul', 'three':"set"}
print('d :', d)
print('type(d) :', type(d))
print(d['two'])
# print(d['hana']) #KeyError
d['four'] = 'net'
print('d :', d)
d['one'] = 1
print('d :', d)
print('len(d) :', len(d))
print('d["three"] :', d['three'])
print('len(d["three"]) :', len(d['three']))
print("'one' in d :", 'one' in d)
print("'dul' in d :", 'dul' in d)
print('d.keys() :', d.keys())
print('d.values() :', d.values())
print('d.items() :', d.items())

print()

d = {}
w1 = "Hello"
w2 = "World~~"
d[w1] = len(w1)
d[w2] = len(w2)
print('d :', d)

d = dict(one = 1, two = 2)
print('d :', d)
d = dict((('one', 1), ('two', 2)))
print('d :', d)


d = {}
total = 0
while True :    
    name = input('이름 입력 : ')
    if(name == '') :
        break
    score = int(input('점수 입력 : '))
    d[name] = score
print('d :', d)
for i in d :
    print('이름 :', i, ' 점수 :', d[i])
    total += d[i]
print('total :', total)
print()
for i, j in d.items() :
    print('이름 :', i, ' 점수 :', j)