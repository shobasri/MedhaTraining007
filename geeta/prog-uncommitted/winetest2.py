import urllib2
import json
import re


baseURL = "http://medhaws.cloudapp.net:3000"
getURL = baseURL+'/wines'

f = urllib2.urlopen(getURL)

responsedata = f.read()

fh = open('response.txt','w')
fh.write(responsedata)
fh.close()

p = re.compile("\s*\"year\:\"2009")
rf = open('response.txt','r')
count = 0
for i in rf:
	i=i.rstrip()
	m=p.match(i)
	print m
if(m!=None):
	print "able to find ID"
	count = count+1

	print count