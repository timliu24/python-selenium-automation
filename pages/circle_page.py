from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CirclePage(Page):
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")
    GOOGLE_PLAY_BTN = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")

    def click_google_play_btn(self):
        self.wait_element_clickable_click(*self.GOOGLE_PLAY_BTN)

    def verify_google_play_opened(self):
        self.verify_partial_url('https://play.google.com/store/apps/')

    def verify_can_click_thru_tabs(self):
        self.wait_element_clickable(*self.BONUS_TAB)

        tabs = self.find_elements(*self.TABS)
        current_url = ''

        for i in range(len(tabs)):
            # Search for tabs before every click to avoid StaleElementReferenceException
            tabs = self.find_elements(*self.TABS)
            tabs[i].click()

            self.wait_url_changes(current_url)
            current_url = self.driver.current_url
