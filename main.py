from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#setup
DRIVER_PATH = "D:\Code\instaBot\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)

#get login and password
with open("config.txt",'r',encoding="utf-8") as f: 
    content = f.readlines()
    LOGIN = content[0]
    PASSWORD = content[1]

#links to get subs
links = ["https://www.instagram.com/donstroy_msk/","https://www.instagram.com/gkpik/"]

#authorization
driver.get("https://www.instagram.com/")
time.sleep(0.7)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(LOGIN)
password.send_keys(PASSWORD)
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(3)

class Account():
    def __init__(self,link):
        self.link = link

    def printSubs(self):
        driver.get(link)
        driver.find_element_by_xpath("//header/section/ul/li[2]/a").click()
        time.sleep(1)
        #elScroll = driver.find_element_by_class_name("jSC57")
        while(True):
            driver.execute_script('document.getElementsByClassName("isgrP")[0].scrollTop = document.getElementsByClassName("isgrP")[0].scrollHeight')
        
for link in links:
    print(link)
    Account(link).printSubs()
time.sleep(2)
driver.close()
