import MySQLdb
db=MySQLdb.connect(host="localhost",user="shoba",passwd="admin",db="test")
c=db.cursor()
c.execute("SELECT * FROM testcase_table")
heads = [d[0] for d in c.description]
c.fetchall()
for row in c:
   print dict(zip(heads,row))
db.close()