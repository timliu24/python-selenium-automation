from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_TAB = (By.XPATH, "//span[text()='Sign in']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart(self):
        self.wait_element_clickable_click(*self.CART_ICON)
        sleep(3)

    def click_on_sign_in_tab(self):
        self.wait_element_clickable_click(*self.SIGN_IN_TAB)
        sleep(3)