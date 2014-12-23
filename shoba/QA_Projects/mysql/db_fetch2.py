import mysql
import sys
import MySQLdb

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
tablepointer = dbvar.cursor()

def getdeails(tp_id):
	try:
		dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
		tablepointer = dbvar.cursor()
		tablepointer.execute("SELECT TestCaseID, last_ran,Testcase_status FROM testcase_table where TstPlanID like (%s)",( tp_id) )
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
	print tp_id
	ln= len(tp_id)
print "lenght of table is   :  ",ln	
for ids in tp_id:
	data= getdeails(tp_id)
print data

	
	
	