'''
Created on 2024. 8. 7.

@author: user
'''
# sungjuk.txt(r) => sungjuk_result.txt(w)

# 이름    국어    영어    수학    합계
# 웬디    77    88    99    264
# 정국    32    90    84    206

fr = open('sungjuk.txt','r',encoding='utf-8')
fw = open('sungjuk_result.txt','w',encoding='utf-8')

s = fr.readline()
fw.write(s) # 이 국 영 수학
fw.seek(fw.tell()-2)

fw.write('\t합계\n')

for line in fr.readlines() :
    total = 0
    # print(line)
    fw.write(line)
    s = line.split()
    print('s:' , s,s[1])
    for i in range(1,len(s)) :
        total += int(s[i])
        # total +"\n"
    fw.seek(fw.tell()-2)
    fw.write('\t'+str(total)+'\n')
    
fr.close()
fw.close()


