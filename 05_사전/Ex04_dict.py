'''
Created on 2024. 8. 6.

@author: user
'''

d = {}
while True :
    word = input('단어:')
    if word == '' :
        break
    mean = input('뜻:')
    d[word]=mean

print('d:',d)

while True : 
    flag = False;
    word = input('찾는 단어:')
    if word.lower() == 'stop' :
        break
    
    for i,key in enumerate(d):
        if word.lower() == key.lower() :
            print('뜻 : ' , d[key],'입니다.')
            flag = True
            break
    
    # for k, v in d.items() :
    #     if k == word:
    #         print("찾는 단어는 ", v, "입니다.")
    #         flag = True
    #         break
        
    if flag == False :
        print('찾는 단어 없습니다.')
    
print('단어 검색을 마칩니다.')
  
    
    
    
    
    
    
    


