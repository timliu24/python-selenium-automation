from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='styles__ButtonWrapper'] img")
SELECTED_OPTION = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@then('User can click and verify through options')
def click_and_verify_through_options(context):
    expected_options= ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_options = []

    options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in options:
        option.click()
        selected_option = context.driver.find_element(*SELECTED_OPTION).text
        selected_option = selected_option.split('\n')[1]
        actual_options.append(selected_option)
        print(actual_options)

    assert expected_options == actual_options, f'Expected {expected_options} did not match actual {actual_options}'