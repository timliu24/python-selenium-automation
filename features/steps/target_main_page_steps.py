from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
CIRCLE = (By.ID, 'utilityNav-circle')

@given('Open Target main page')
def open_target_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('Click on Sign In tab')
def click_on_sign_in_tab(context):
    context.app.header.click_on_sign_in_tab()


@when('Click on Target Circle tab')
def click_on_target_circle_tab(context):
    context.driver.find_element(*CIRCLE).click()
    sleep(2)


@then('Verify header in shown')
def verify_header(context):
    # header = context.driver.find_element(*HEADER)
    # print(header)
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'