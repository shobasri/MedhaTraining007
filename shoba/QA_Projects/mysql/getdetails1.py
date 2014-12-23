import MySQLdb
import json

table_data=[]
def create_json():
 js=json.dumps(table_data)
 json_obj=json.loads(js)
 print "this is testplan details in json format ---------->   " ,json_obj
 print  " this is json obj    ", json_obj[0]['TestPlanID']

db=MySQLdb.connect(host="localhost",user="shoba",passwd="admin",db="test")
c=db.cursor()
c.execute("SELECT * FROM testcase_table")
heads = [d[0] for d in c.description]
c.fetchall()
for row in c:
   table_data.append(dict(zip(heads,row)))
print "this is testplan detail in dictionary format  --------->  " ,table_data
print "      ======================================================\n "
create_json()
db.close()