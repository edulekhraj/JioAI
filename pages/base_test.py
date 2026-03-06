from pages.login_page import LoginPage


class BaseTest:

    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    # @property
    # def dashboard_page(self):
    #     return DashboardPage(self.driver)
    #
    # @property
    # def book_page(self):
    #     return BookPage(self.driver)