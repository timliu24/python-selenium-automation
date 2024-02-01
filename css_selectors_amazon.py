from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')
#Create account
driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small')
#Your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
#Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')
#Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#Password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, '.auth-inlined-information-message .a-box-inner.a-alert-container')
#Re-enter Password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
#Create your Amazon account
driver.find_element(By.CSS_SELECTOR, '#continue')
#Condition of Use
driver.find_element(By.CSS_SELECTOR, '[href*=condition_of_use]')
#Privacy Notice
driver.find_element(By.CSS_SELECTOR, '[href*=notification_privacy_notice]')
#Sing in
driver.find_element(By.CSS_SELECTOR, '[href*=signin]')