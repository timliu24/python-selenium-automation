from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Sign In')
def click_on_sign_in(context):
    context.app.sign_in_window.click_on_sign_in()


@then('Verify Sign into your Target account form open')
def verify_sign_in_form_open(context):
    context.app.sign_in_window.verify_sign_in_form_open()
    # expected_text = "Sign into your Target account"
    # current_text = context.driver.find_element(*SIGN_IN_FORM).text
    # assert expected_text in current_text
    # print(f"Found '{expected_text}'.")
