from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

driver = webdriver.Chrome('chromedriver.exe')
actions = ActionChains(driver)
driver.get("https://messenger.com")

email_field = driver.find_element(By.XPATH, "//*[@id='email']")
password_field = driver.find_element(By.XPATH, "//*[@id='pass']")

user_email = input("enter email: ")
user_password = input("enter password: ")
message = input("enter message: ")
recipient = input("enter recipient's full name: ")

email_field.send_keys(user_email)
password_field.send_keys(user_password)

time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='loginbutton']").click()

time.sleep(4)

current_chat_name = driver.find_element(By.XPATH, "//*[@id='js_5']/span").text
print(current_chat_name)

if current_chat_name != recipient:
    search_field = driver.find_element(By.XPATH, "//*[@id='js_u']/div/div/div[1]/span[1]/label/input")
    search_field.click()
    search_field.send_keys(recipient)
    time.sleep(2)
    recipient_chat = driver.find_elements(By.CLASS_NAME, "_8slc")[1]
    recipient_chat.click()

actions.send_keys(message)
actions.send_keys(Keys.ENTER)

curr_time = datetime.datetime.now()
send_time = datetime.datetime(2020, 8, 9, 11, 8)
while curr_time < send_time:
    curr_time = datetime.datetime.now()
    print(curr_time)
actions.perform()

