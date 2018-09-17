import pymysql
'''
#连接数据库
con = pymysql.connect(host='localhost',
                       user='user',
                       password='123456',
                       db='personnel_man',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
try:
    with con.cursor() as cursor:
        #读取单条记录
        sql = "select 'd_no','d_name','s_no' from 'department' "
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    con.close()

'''
db = pymysql.connect("localhost","user","123456","personnel_man")

cursor = db.cursor()
try:
    cursor.execute("select * from department")
    results=cursor.fetchall()
    for row in results:
        dno = row[0]
        dname = row[1]
        sno = row[2]
        print(dname)
except:
    print("error")
db.close()
