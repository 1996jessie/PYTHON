'''
Created on 2024. 8. 6.

@author: user
'''
d = {'윤아':30,"태연":20,"정국":50}
print('d:',d)

# 태연의 나이 출력
print(d.get("태연"))
print(d['태연'])
print(d.keys())
print(d.values())

for i in d.keys() :
    print(i,end=' ')
print()
    
for i in d.values() :
    print(i,end=' ') 
print()

for i in d :
    print(i,end=' ')
print()    

for i in d.items() :
    print(i,':',i[0],'/',i[1])
print()

for i,j in d.items() :
    print(i,j)
print()

for i,j in enumerate(d):
    print(i,j,d[j])




       