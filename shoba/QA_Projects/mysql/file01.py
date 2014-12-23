# getting data from table in dict format...and seperating dict with comma,doing json 
import MySQLdb
import json
table_dict=[]

def create_json():
 js=json.dumps(table_dict)
 json_obj=json.loads(js)
# print "this is final json --",json_obj
 print json_obj[1]['UserId']

db=MySQLdb.connect(host="localhost",user="root",passwd="admin",db="framework")
c=db.cursor()
c.execute("SELECT * FROM userprofile")
heads = [d[0] for d in c.description]
#print c.description
c.fetchall()