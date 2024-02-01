from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign In tab')
def click_on_sign_in_tab(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(1)

@when('Click on Sign In')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify Sign into your Target account form open')
def verify_sign_in_form_open(context):
    expected_text = "Sign into your Target account"
    current_text = context.driver.find_element(By.XPATH, "//div[@class='styles__ContentWrapper-sc-19gc5cv-1 CpfGf']").text
    assert expected_text in current_text
    print(f"Found '{expected_text}'.")