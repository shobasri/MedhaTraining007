import mysql
import MySQLdb
import json

table_data=[]

def getdetails(tp_Id):
    dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
    tablepointer = dbvar.cursor()    
    try:
	tablepointer.execute("SELECT * from testcase_table") 
	heads = [d[0] for d in tablepointer.description]
	tablepointer.fetchall()
	
	tablepointer.fetchall()
	for row in tablepointer:
	  print dict(zip(heads,row))	
	    return testcaseDetails
    except:
	print "not in records"
    else:
	print "end of script"   
	fh= open('testplan_id.csv','r')
	tp_id =[]
	for i in fh:
		i=i.rstrip()
		i=i.split(',')
		tp_id=i
		ln= len(tp_id)
	print "lenght of table is   :  ",ln	
	for ids in tp_id:
		data= getdeails(tp_id)	
	print data
	