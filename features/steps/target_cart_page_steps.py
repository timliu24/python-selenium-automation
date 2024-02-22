from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on Options")
def click_on_options(context):
    context.app.cart_option_window.click_on_options()


@when("Click Add to cart bar")
def click_add_to_cart_bar(context):
    context.app.cart_option_window.click_add_to_cart_bar()


@when("Click View cart and check out")
def click_view_cart_and_check_out(context):
    context.app.cart_option_window.click_view_cart_and_check_out()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


@then("Verify cart have items")
def verify_cart_have_items(context):
    context.app.cart_page.verify_cart_have_items()