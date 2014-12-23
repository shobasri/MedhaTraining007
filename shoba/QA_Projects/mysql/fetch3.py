import mysql
import sys
import MySQLdb

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql

tablepointer = dbvar.cursor()
def getdeails(tp_id):
	try:
		tablepointer.execute("SELECT * from testcase_table") 
		testcaseDetails = tablepointer.fetchall()
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
outputdata={}
for idvalue in data:
	tmp = []
	for eachVal in idvalue:
		tmp.append(eachVal)
print tmp

def getcolumn_names():
	try:
		tablepointer.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'testcase_table' ")  #writing into table
		col_name = tablepointer.fetchall()
		print col_name
	except:
		print "not in records"
	else:
		print "end of script"