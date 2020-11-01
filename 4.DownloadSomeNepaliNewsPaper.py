import requests #for website
import numpy as np
import os #for defining the path
from datetime import date
from selenium import webdriver 

#for Kantipur and Kathmandu post
user = "dzieulaatbuursfzaz@wqcefp.online"
passwrd = "1234567890"

today = date.today()
d3 = today.strftime("%Y-%m-%d")
#print(d3)

urlkan = "https://epaper.ekantipur.com/kantipur/download/" + str(d3)	
kan = requests.get(urlkan, allow_redirects = True)
open("D:/todayPaper/Kantipur_daily."+ str(d3)+'.pdf', 'wb').write(kan.content)

urlktmpost = "https://epaper.ekantipur.com/kathmandupost/download/" + str(d3)	
kan = requests.get(urlktmpost, allow_redirects = True)
open("D:/todayPaper/KathmanduPost_daily."+ str(d3)+'.pdf', 'wb').write(kan.content)	
	

##for Gorkhapatra 
driver = webdriver.Firefox(executable_path="D:/OneDrive - ICIMOD/python/seleniumGekoDriver/geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(1)

driver.get("https://gorkhapatraonline.com/gkppdf/gorkhapatra")

urlgor = driver.find_elements_by_xpath("/html/body/div[2]/div/div[1]/a/div[1]/img")[0]
urlgor.click()
driver.switch_to.window(driver.window_handles[1])

driver.implicitly_wait(30)

URL = driver.current_url
Segments = URL.rpartition('/')
pdfID = Segments[2]

url2 = "https://gorkhapatraonline.com/ArchiveNewsFile/"	+ pdfID
gp = requests.get(url2, allow_redirects = True)
open("D:/todayPaper/Gorkhapatra_daily_"+str(d3)+ ".pdf", mode="wb").write(gp.content)

driver.close()
driver.quit()
	

#for Nepali times need to update the numbers 
ID = np.arange(1032,1034) # the id for "16 - 22 October 2020" is 1032,  i dont know how the numbers are arranged therefore thought to download few of the latest 
for i in ID:
	url = "http://himalaya.socanth.cam.ac.uk/collections/journals/nepalitimes/pdf/Nepali_Times_" + str(i) + ".pdf"	
	r = requests.get(url, allow_redirects = True)
	open("D:/todayPaper/Nepali_times_weekly."+ str(i)+'.pdf', 'wb').write(r.content)


### alternaive better way, working 
driver = webdriver.Firefox(executable_path="D:/OneDrive - ICIMOD/python/seleniumGekoDriver/geckodriver.exe")
driver.maximize_window()
#driver.set_window_position(200, 1)

driver.get("https://www.nepalitimes.com/")

urlgor = driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div/main/section[1]/div/div[1]/div[2]/div[1]/div[6]/a")[0]
urlgor.click()

driver.switch_to.window(driver.window_handles[1])

driver.implicitly_wait(20)

url3 = driver.current_url

gp = requests.get(url3, allow_redirects = True)
open("D:/todayPaper/NepaliTimes_weekly"+str(d3)+ ".pdf", mode="wb").write(gp.content)

driver.close()
driver.quit()















##for himalayan times it seems it is based on the multiple images. Therefore I was not able to download as pdf at the moment. 
##https://epaper.thehimalayantimes.com/get_image.aspx?w=280&eid=7659e3a2-13e4-41e2-9fe3-ebff9260fa28
	
##for Nagarik Also I was not able to downlaod the pdf due to the page being the php file. COuldn't convert it to the pdf. 
# # user = "tbvzsrbyouzvfaimdw@avxrja.com"
# # passwrd = "1234567890"
# # urlnag = "https://epaper.nagariknetwork.com/nagarik/src/epaper.php?id=4482"	
