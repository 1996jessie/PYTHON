'''
Created on 2024. 8. 9.

@author: user
'''
import cx_Oracle
con = cx_Oracle.connect('sqlid/sqlpw@localhost:1521/orcl') 

cur = con.cursor()
try :
    cur.execute('drop table sungjuk')
except cx_Oracle.DatabaseError:
    print("sungjuk 테이블 존재하지 않음")
    
createSungjuk = '''
    create table sungjuk(
        name varchar2(10),
        kor number,
        eng number
    )
'''
cur.execute(createSungjuk)

insertSungjuk = "insert into sungjuk values('김연아', 80, 90)"
cur.execute(insertSungjuk)
insertSungjuk = "insert into sungjuk values('손흥민', 90, 60)"
cur.execute(insertSungjuk)
cur.execute('commit')

selectSungjuk = "select * from sungjuk"
cur.execute(selectSungjuk)
for row in cur :
    print(row)

print('--------------')
    
L = [('나연', 33, 77), ('설현', 77, 88)]
cur.executemany('insert into sungjuk values (:1, :2, :3)', L)
cur.execute('commit')


selectSungjuk = "select * from sungjuk order by name desc"
cur.execute(selectSungjuk)
for row in cur :
    print(row)
    
print('--------------')

cur.execute("select * from sungjuk order by name desc")
print(cur.fetchone())
print('--------------')
print(cur.fetchall())

print('--------------')

eng1= 70
eng2 = 89
cur.execute("select * from sungjuk where eng between :1 and :2", (eng1, eng2))
print('between :', cur.fetchall())
cur.execute("select * from sungjuk where eng >= :1 and eng <= :2", (eng1, eng2))
print('부등호 :', cur.fetchall())
cur.execute("select * from sungjuk where eng >= %d and eng <= %d" % (eng1, eng2))
print('%d :', cur.fetchall())

print('--------------')

update_name = "설현"
update_kor = 100
cur.execute("update sungjuk set kor = :1 where name = :2",(update_kor, update_name))
cur.execute(selectSungjuk)
print('update :', cur.fetchall())
cur.execute("update sungjuk set kor = %d where name = '%s'" % (update_kor, update_name))
cur.execute(selectSungjuk)
print('update % :', cur.fetchall())

print('--------------')

delete_name = "손흥민"
cur.execute("delete from sungjuk where name = :1", (delete_name,))
cur.execute(selectSungjuk)
print('delete :', cur.fetchall())
cur.execute("delete from sungjuk where name = '%s'" % (delete_name,))
cur.execute(selectSungjuk)
print('delete % :', cur.fetchall())

print('--------------')

con_name = "연"
cur.execute("select * from sungjuk where name like :1", ("%" + con_name + "%",))
print('select연 :', cur.fetchall())

print('--------------')