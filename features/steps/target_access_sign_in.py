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


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    # print('Current window', context.original_window)
    # print('All windows:', context.driver.window_handles)


@when('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_on_target_terms_and_conditions_link()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.circle_page.switch_to_new_window()
    # print('After switching to a new window:')
    # print('All windows:', context.driver.window_handles)
    # print('Current window', context.driver.current_window_handle)


@then('Verify Terms and Conditions page is opened')
def verify_term_and_conditions_page_is_opened(context):
    context.app.sign_in_page.verify_term_and_conditions_page_is_opened()


@then('Close current window')
def close(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.circle_page.switch_to_window_by_id(context.original_window)
    # print('After switching back:')
    # print('Current window', context.driver.current_window_handle)
