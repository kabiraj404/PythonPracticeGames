import requests 
import numpy as np
import os 
import time 
from datetime import date
from selenium import webdriver 

#for Kantipur and Kathmandu post
user = "dzieulaatbuursfzaz@wqcefp.online"
passwrd = "1234567890"

today = date.today()
d3 = today.strftime("%Y-%m-%d")

urlkan = "https://epaper.ekantipur.com/kantipur/download/" + str(d3)	
kan = requests.get(urlkan, allow_redirects = True)
open("D:/todayPaper/Kantipur_daily."+ str(d3)+'.pdf', 'wb').write(kan.content)

urlktmpost = "https://epaper.ekantipur.com/kathmandupost/download/" + str(d3)	
kan = requests.get(urlktmpost, allow_redirects = True)
open("D:/todayPaper/KathmanduPost_daily_"+ str(d3)+'.pdf', 'wb').write(kan.content)	
	
##for karobar dailey
d4 = today.strftime("%d-%b-%Y")
year = today.strftime("%Y")
month = today.strftime("%m")

urlkarobar = "https://www.karobardaily.com/wp-content/uploads/" + str(year) + "/" + str(month) + "/Karobar-" + str(d4) + ".pdf"
karobar = requests.get(urlkarobar, allow_redirects = True)
open("D:/todayPaper/Karobar_daily_"+ str(d3)+'.pdf', 'wb').write(karobar.content)	


##for Gorkhapatra 
driver = webdriver.Firefox(executable_path="D:/OneDrive - ICIMOD/python/seleniumGekoDriver/geckodriver.exe")
driver.set_window_position(1, 1)
driver.implicitly_wait(5)

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
	

#for Nepali times 
driver = webdriver.Firefox(executable_path="D:/OneDrive - ICIMOD/python/seleniumGekoDriver/geckodriver.exe")
driver.set_window_position(1, 1)

driver.get("https://www.nepalitimes.com/")
urlgor = driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div/main/section[1]/div/div[1]/div[2]/div[1]/div[6]/a")[0]
urlgor.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
url3 = driver.current_url

gp = requests.get(url3, allow_redirects = True)
open("D:/todayPaper/NepaliTimes_weekly_"+str(d3)+ ".pdf", mode="wb").write(gp.content)

driver.close()
driver.quit()

print("Yahoo!! you have successfully downloaded Kantipur, Kathmandu Post, Gorkhapatra, Karobar and Nepali Times pdf") 