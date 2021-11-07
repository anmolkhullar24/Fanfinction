from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options,executable_path=r"E:/WORK/chromedriver_win32/chromedriver_win32/chromedriver")
driver.get("https://www.fanfiction.net/s/11767990/19/The-Marriage-Decree")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.implicitly_wait(10)
driver.execute_script("window.open('https://www.fanfiction.net/s/11767990/19/The-Marriage-Decree');")
fileToWrite = open("fanfiction.html", "w")
for i in range(132):
	s="https://www.fanfiction.net/s/11767990/"+str(i+1)+"/The-Marriage-Decree"
	driver.get(s)
	time.sleep(5)
	multiple_elements = driver.find_elements_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[6]/div[1]")
	if len(multiple_elements) == 1:
		print(i+1)
	element=multiple_elements[0].get_attribute('outerHTML')
	fileToWrite.write(element)
	fileToWrite.write("<br>")
fileToWrite.close()
print("done")