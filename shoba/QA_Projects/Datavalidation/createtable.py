#checking for given name present in the table or not
import MySQLdb
import sys
import re

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
tablepointer = dbvar.cursor()#command to enable cursor
try:
	tablepointer.execute("select #checking for given name present in the table or not
import MySQLdb
import sys
import re

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
tablepointer = dbvar.cursor()#command to enable cursor
#checking for given name present in the table or not
import MySQLdb
import sys
import re

dbvar = MySQLdb.connect("localhost","shoba","admin","test")#to build the connection between python and mysql
tablepointer = dbvar.cursor()#command to enable cursor

try:
	tablepointer.execute("select * from userprofile ) #writing into table
	data = tablepointer.fetchall()
	print data
except:
	print "not in records"
	
else:
	print "end of script"





try:
	tablepointer.execute("select userName from profile1 where userName like %s",( name)) #writing into table
	#data = tablepointer.fetchall()
	print data
except:
	print "not in records"
	name =raw_input("enter your first name")
	ls_name =raw_input("enter your last name")
	contact =raw_input("enter your  contact")
	email =raw_input("enter your email")
	
	#tablepointer.execute("insert into profile1 (userName ) VALUES (%s) ",(name)) #writing into table
	tablepointer.execute("insert into profile1 (userName ,lastName,contact,Email) VALUES (%s,%s,%d,%s)",(name,ls_name,contact,email))															
else:
	tablepointer.execute("select * from profile1")




 from profile1 where userName like %s",( name)) #writing into table
	#data = tablepointer.fetchall()
	print data
except:
	print "not in records"
	name =raw_input("enter your first name")
	ls_name =raw_input("enter your last name")
	contact =raw_input("enter your  contact")
	email =raw_input("enter your email")
	
	#tablepointer.execute("insert into profile1 (userName ) VALUES (%s) ",(name)) #writing into table
	tablepointer.execute("insert into profile1 (userName ,lastName,contact,Email) VALUES (%s,%s,%d,%s)",(name,ls_name,contact,email))															
else:
	tablepointer.execute("select * from profile1")




