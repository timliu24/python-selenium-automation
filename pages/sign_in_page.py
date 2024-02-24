from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    TERM_AND_CONDITIONS = (By.XPATH, "//a[@aria-label='terms & conditions - opens in a new window']")

    def click_on_target_terms_and_conditions_link(self):
        self.click(*self.TERM_AND_CONDITIONS)

    def verify_term_and_conditions_page_is_opened(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions/')
