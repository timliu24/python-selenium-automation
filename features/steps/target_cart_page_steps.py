from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@when("Click on Options")
def click_on_options(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']").click()


@when("Click Add to cart bar")
def click_add_to_cart_bar(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='shippingButton']").click()


@when("Click View cart and check out")
def click_view_cart_and_check_out(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


@then("Verify cart have items")
def verify_cart_have_items(context):
    cart_total = context.driver.find_element(By.CSS_SELECTOR, ".h-margin-b-tight.h-text-grayDark").text
    assert "subtotal" and "item" or "items" in cart_total, f"Cart total not found."