from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CIRCLE_BENEFITS = (By.CSS_SELECTOR, "[class*='styles__BenefitCardHeading']")


@then('Verify {expected_amount} benefit boxes')
def verify_circle_benefits(context, expected_amount):
    expected_amount = int(expected_amount)
    circle_benefits = context.driver.find_elements(*CIRCLE_BENEFITS)
    assert len(circle_benefits) == expected_amount, f'Expected {expected_amount} links, but got {len(circle_benefits)}'


@then('Verify that clicking though Circle tabs works')
def verify_can_click_thru_tabs(context):
    context.app.circle_page.verify_can_click_thru_tabs()


@when('Click Google Play button')
def click_google_play_btn(context):
    context.app.circle_page.click_google_play_btn()


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    context.app.circle_page.verify_google_play_opened()
