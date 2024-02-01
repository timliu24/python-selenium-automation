from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(3)


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert 'empty' in actual_text, f'Expected word empty not in {actual_text}'
    print('Test case passed')