from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Webdrivers\chromedriver.exe")

driver.get("https://facebook.com")
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

username.send_keys(os.environ.get("FACEBOOK_EMAIL"))
password.send_keys(os.environ.get("FACEBOOK_PASS"))
password.send_keys(Keys.ENTER)
