from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
FOLGERS_CLASSIC_MEDIUM = (By.ID, 'addToCartButtonOrTextIdFor13397813')
DENIZEN_FROM_LEVIS_MENS_285 = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")


@when('Click Add to cart icon on {product}')
def click_add_to_cart_icon(context, product):
    context.driver.find_element(*FOLGERS_CLASSIC_MEDIUM).click()


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@when ('Click on {product}')
def click_on_product(context, product):
    context.driver.find_element(*DENIZEN_FROM_LEVIS_MENS_285).click()
    sleep(6)
