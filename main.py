from selenium import webdriver
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
links = ["https://www.instagram.com/gkpik/followers/"]

#authorization
driver.get("https://www.instagram.com/")
time.sleep(0.7)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(LOGIN)
password.send_keys(PASSWORD)


class Account():
    def __init__(self,link):
        self.link = link
    def printSubs(self):
        driver.get(link)
        time.sleep(1)
        


# for link in links:
#     acc = Account(link)
#     acc.printSubs()
