from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CIRCLE_BENEFITS = (By.CSS_SELECTOR, "[class*='styles__BenefitCardHeading']")


@then('Verify {expected_amount} benefit boxes')
def verify_circle_benefits(context, expected_amount):
    expected_amount = int(expected_amount)
    circle_benefits = context.driver.find_elements(*CIRCLE_BENEFITS)
    assert len(circle_benefits) == expected_amount, f'Expected {expected_amount} links, but got {len(circle_benefits)}'