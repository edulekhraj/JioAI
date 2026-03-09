from pages.login_page import LoginPage
from pages.profile_menu import ProfileMenu


class BaseTest:

    def __init__(self, driver):
        self.driver = driver
        self._login_page = LoginPage(driver)
        self._profile_menu = ProfileMenu(driver)

    @property
    def login_page(self):
        return self._login_page

    @property
    def profile_menu(self):
        return self._profile_menu
