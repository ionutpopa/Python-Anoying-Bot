from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\\webdrivers\\chromedriver.exe"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(PATH, chrome_options=options)

driver.get("https://www.messenger.com/t/example") # change the link with one that is available
user = driver.find_element_by_id("email")
user.send_keys("your-facebook-user-name") # introduce your facebook user name, if you don't know you can find it in your facebook profile link
password = driver.find_element_by_id("pass")
password.send_keys("your-facebook-password") # introduce your facebook password
password.send_keys(Keys.RETURN)

with open("vechiul_testament.txt", 'r') as text_to_send: # change vechiul_testament.txt with your txt file
    data = text_to_send.read().split()
    for lines in data:
        imputmessenger = driver.find_element_by_xpath("//div[@class='_1mf _1mj']")
        imputmessenger.send_keys(lines)
        time.sleep(1)
        enterMessage = driver.find_element_by_xpath("//a[@class='_30yy _38lh _7kpi']")
        enterMessage.send_keys(Keys.RETURN)

driver.quit()