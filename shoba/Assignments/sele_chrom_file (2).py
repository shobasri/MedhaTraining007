import selenium
from selenium import webdriver
def assertCheck(actual,expected):
	if (actual==expected):
		return True
	else:
		return False
chrombr = webdriver.ChromeOptions()
chrombr.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#binary_location is predefine variable to hold the location of binary file
br=webdriver.Chrome("C:\Users\Shoba\Downloads\chromedriver_win32\chromedriver.exe",chrome_options = chrombr)
br.get("http://bing.com")
br.implicitly_wait(30)	
userName = br.find_element_by_class_name("b_searchbox")
print userName
br.close()
#id = br.find_element_by_id("sb_form_q")
#print id
#print assertCheck("b_searchbox",userName)
#print assertCheck("sb_form_q",id)


	




 