'''
Created on 2024. 8. 9.

@author: user
'''

import cx_Oracle
con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl')  

print(type(con))

cur = con.cursor()


try:
    dropseq = 'drop sequence per_seq'
    cur.execute(dropseq)
except cx_Oracle.DatabaseError:
    print("per_seq 시퀀스 존재하지 않음")

try:
    drop = 'drop table person'
    cur.execute(drop)
except cx_Oracle.DatabaseError:
    print("person 테이블 존재하지 않음")

seq = 'create sequence per_seq'
cur.execute(seq)

create = '''create table person (
    num number primary key,
    id varchar2(10),
    name varchar2(10),
    addr varchar2(10)
)
'''
cur.execute(create)

cur.execute('select * from person')
for row in cur :
    print('row : ', row)
print('----------------------')

insert = "insert into person values(per_seq.nextval, 'kim', '연아', '한국')"
cur.execute(insert)
insert = "insert into person values(per_seq.nextval, 'son', '흥민', '영국')"
cur.execute(insert)
insert = "insert into person values(per_seq.nextval, 'park', '찬호', '미국')"
cur.execute(insert)

# con.commit()
cur.execute('commit')

cur.execute('select * from person')
for row in cur :
    print('row : ', row, '/', row[2])
print('----------------------')

updatehong = "update person set id = 'hong' where id = 'kim'"
cur.execute(updatehong)

con.commit()

deletepark = "delete from person where id = 'park'"
cur.execute(deletepark)
con.commit()
cur.execute('select * from person')
for row in cur :
    print('row : ', row)
print('----------------------')

cur.close()
con.close()