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

# 1. Open the url
driver.get('https://www.target.com/')
# 2. Click SignIn button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
# 3. Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)
# 4. Verify SignIn page opened:
# “Sign into your Target account” text is shown,
expected_text = "Sign into your Target account"
current_text = driver.find_element(By.XPATH, "//div[@class='styles__ContentWrapper-sc-19gc5cv-1 CpfGf']").text
assert expected_text in current_text
print(f"Found '{expected_text}'.")
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)field
assert driver.find_element(By.ID, 'login').is_displayed()
print("'Sign in' button is shown.")