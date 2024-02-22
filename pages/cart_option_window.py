from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartOptionWindow(Page):
    CLICK_ADD_TO_CART_BAR = (By.XPATH, "//button[@data-test='shippingButton']")
    CLICK_ON_CART_OPTIONS = (By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
    CLICK_VIEW_CART_AND_CHECK_OUT = (By.XPATH, "//a[text()='View cart & check out']")
    def click_on_options(self):
        self.click(*self.CLICK_ON_CART_OPTIONS)

    def click_add_to_cart_bar(self):
        self.click(*self.CLICK_ADD_TO_CART_BAR)

    def click_view_cart_and_check_out(self):
        self.click(*self.CLICK_VIEW_CART_AND_CHECK_OUT)