import mysql
import sys
import MySQLdb

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
tablepointer = dbvar.cursor()
def getdeails(tp_id):
	try:
		dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
		tablepointer = dbvar.cursor()
		tablepointer.execute("""SELECT TestCaseID, last_ran,Testcase_status FROM testcase_table JOIN testplan_table ON
		testcase_table.TestPlanId = testplan_table.TestPlanID""") 
		heads = [d[0] for d in tablepointer.description]
		tablepointer.fetchall()
		for row in tablepointer:
			print dict(zip(heads,row))
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

