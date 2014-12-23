import selenium

from selenium import webdriver
browser= webdriver.Firefox()
browser.get("http://bing.com")
#finding the id element which is "username"
browser.implicitly_wait(10)
print "loading to the elements"

try :
	userName = browser.find_element_by_id("username")
	print "loading to the elements"
except:
	print "not able to find username", 
else:
	print ("able to find userName", userName)
browser.close()	
