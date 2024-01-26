#Practice
#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
#Email field
driver.find_element(By.ID, "//input[@id='ap_email']")
#Continue button
driver.find_element(By.ID, "//input[@id='continue']")
#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#Forgot your password link
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")
#Other issues with Sign-In link
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")
#Create your Amazon account button
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")