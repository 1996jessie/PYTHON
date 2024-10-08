'''
Created on 2024. 8. 13.

@author: user
'''

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt

font_location='c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)


from bs4 import BeautifulSoup
import urllib.request

import cx_Oracle
con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl')  

cur = con.cursor()


try:
    drop = 'drop table movie'
    cur.execute(drop)
except cx_Oracle.DatabaseError:
    print("movie 테이블 존재하지 않음")
    

createMovie = '''create table movie (
    title varchar2(50),
    grade number
)
'''
cur.execute(createMovie)


# fp = open('example.html')
with open('example.html') as fp :
    soup = BeautifulSoup(fp,'html.parser')
    
    print('1:', soup)
    print('2:', soup.title)
    print('3:', soup.title.name)
    print('4:', soup.title.string)
    print('5:', soup.title.getText())
    print('6:', soup.title.parent.name)
    print('7:', soup.p)
    print('8:', soup.div)
    print('9:', soup.find_all('div'))
    print('10:', soup.find_all('p'))
    print('11:', soup.find_all('div','ex_class'))
    print('12:', soup.find())
    print('13:', soup.find(id='ex_id'))
    print('14:', soup.find_all(id='ex_id'))
    print('15:', soup.find_all('div', id='ex_id'))

# fp.close()

print('\n\n\n')

# 파일럿 하나의 일부 정보
# <div class="list_image_box" style="width:670px;"> 
# <ul class="_panel"> 
# <li> 
#      <a nocr onclick="return goOtherCR(this, 'a=nco_x0a*M.boxschinfo&r=1&i=1800009D_000000000000&u=' + urlencode(this.href));" href="?where=nexearch&sm=tab_etc&mra=bkEw&pkid=68&os=26098746&qvt=0&query=%ED%8C%8C%EC%9D%BC%EB%9F%BF" class="inner"> 
#         <div class="item"> 
#              <div class="thumb"> 
#                  <span class="cm_thumb_rank_number">
#                     <span class="this_bg"></span>
#                     <span class="this_text">1</span>
#                  </span> 
#                  <img src="https://search.pstatic.net/common?type~~~~.jpg" width="103" height="145" alt="파일럿" 
#                      onerror="this.src='https://ssl~~~no_img.png'"> 
#              </div> 
#              <div class="title_box"> 
#                  <strong class="name">파일럿</strong> 
#                  <span class="sub_text">
#                     <span class="this_icon_star"></span>
#                     7.93
#                 </span> 
#             </div> 
#         </div> 
#     </a> 
# </li>

soup = BeautifulSoup(urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4').read(),'html.parser')
movieList = [] # 제목
gradeList = [] # 평점

result = soup.find_all('strong','name')
print('result:\n', result)
print(len(result)) #52 => 흥행순(30)+평점순(22)
 
count = 0
for n in result :
    # print('n:', n)
    count = count + 1
    if count > 30 :
        # print('n:', n.getText())
        movieList.append(n.getText())
    
     
# 평점 가져와서 출력하기
result = soup.find_all('span','sub_text')
print('result:\n', result)
count = 0
for n in result :
    count = count + 1
    if count > 30 :
        gradeList.append(n.getText())


for i in range(movieList.__len__()) :
    print(movieList[i],' : ',gradeList[i])


insertMovie = 'insert into movie values (:1, :2)'
for i in range(movieList.__len__()) :
    cur.execute(insertMovie, (movieList[i], gradeList[i]))
con.commit()


selectMovie = 'select * from movie'
print("select * from movie 결과")
cur.execute(selectMovie)
for row in cur:
    print(row)

selectTop5Movies = '''
select title, grade
from movie
order by grade desc
fetch first 5 rows only
'''

cur.execute(selectTop5Movies)
rows = cur.fetchall()

df_top_5 = pd.DataFrame(rows, columns=['영화 제목', '평점'])

plt.figure(figsize=(10, 6))
plt.bar(df_top_5['영화 제목'], df_top_5['평점'])
plt.ylabel('평점')
plt.title('matplotlib 예제')

plt.show()

cur.close()
con.close()