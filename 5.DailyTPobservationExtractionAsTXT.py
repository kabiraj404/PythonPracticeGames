
from selenium import webdriver 
import csv
from datetime import date
  
driver = webdriver.Firefox(executable_path="D:/OneDrive - ICIMOD/python/seleniumGekoDriver/geckodriver.exe")

driver.get("http://mfd.gov.np/")

#### cound the number of rows
rows = len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/th"))

##for visulization of the output in the console 
# # for r in range(1, rows+1):
	# # for c in range(1, cols+1):
	
		# # value = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
		# # for i in value: #it helps to print the individual value of the table 
			# # print(i.text, end= ",") ## element wise answer
	# # print() ##breaks the outpur in each row 

today = date.today()
d3 = today.strftime("%Y-%m-%d")

x = open("D:/OneDrive - ICIMOD/DHMdaily/TodaysWeather_" + d3 + ".txt", "w")
#for the date in the first row:
head1 = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/h3")
for i in head1:
	print(i.text, end= ",",file = x) 
#keeping the header for the data 	
print(["Station", "Maximum Temp(°C)", "Minimum Temp(°C)", "24 hrs Rainfall(mm)"], file = x)
#for the data table 
for r in range(1, rows+1):
	for c in range(1, cols+1):
	
		value = driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")
		for i in value: #it helps to print the individual value of the table 
			print(i.text, end= ",", file = x) ## element wise answer
	print(file = x) ##breaks the outpur in each row 

x.close()

print("Thank you the data is inside the DHMdailey folder ordered by each day") 
