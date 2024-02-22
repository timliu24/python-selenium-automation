from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class SignInWindow(Page):
    SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    SIGN_IN_FORM = (By.XPATH, "//div[@class='styles__ContentWrapper-sc-19gc5cv-1 CpfGf']")

    def click_on_sign_in(self):
        self.wait_element_clickable_click(*self.SIGN_IN)

    def verify_sign_in_form_open(self):
        self.verify_partial_text("Sign into your Target account", *self.SIGN_IN_FORM)


