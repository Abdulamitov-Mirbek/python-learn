import psycopg2

con = psycopg2.connect(
            host='localhost',
            dbname='university',
            user='postgres',
            password='farhat141516.pg',
            port='5432',

)
cur = con.cursor()
print('PODKLUTHENO')
cur.execute('select * from  student order by id')

for row in cur:
    print(row)


cur.execute('delete from student where  id=%s',(2,))
con.commit()
# cur.execute('insert into student (name,age,sity) values (%s,%s,%s)',
#             ('Aibek',20,'datha'))
# con.commit()