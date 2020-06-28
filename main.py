from selenium import webdriver

#setup
DRIVER_PATH = "D:\Code\instaBot\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)

driver.get("https://www.instagram.com/")


