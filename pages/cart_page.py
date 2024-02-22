from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_SUBTOTAL_AND_ITEMS = (By.CSS_SELECTOR, ".h-margin-b-tight.h-text-grayDark")

    def verify_cart_empty_message(self):
        actual_text = self.find_element(*self.CART_HEADER).text
        assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"

    def verify_cart_have_items(self):
        cart_total = self.find_element(*self.CART_SUBTOTAL_AND_ITEMS).text
        assert "subtotal" and "item" or "items" in cart_total, f"Cart total not found."