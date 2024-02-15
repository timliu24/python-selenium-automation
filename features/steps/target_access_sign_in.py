from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_FORM = (By.XPATH, "//div[@class='styles__ContentWrapper-sc-19gc5cv-1 CpfGf']")


@when('Click on Sign In')
def click_on_sign_in(context):
    context.wait.until(EC.presence_of_element_located(SIGN_IN), message='Sign in no found.')
    context.driver.find_element(*SIGN_IN).click()
    sleep(2)

@then('Verify Sign into your Target account form open')
def verify_sign_in_form_open(context):
    expected_text = "Sign into your Target account"
    current_text = context.driver.find_element(*SIGN_IN_FORM).text
    assert expected_text in current_text
    print(f"Found '{expected_text}'.")