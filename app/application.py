from pages.base_page import Page
from pages.cart_option_window import CartOptionWindow
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.sign_in_window import SignInWindow


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cart_option_window = CartOptionWindow(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.sign_in_window = SignInWindow(driver)
