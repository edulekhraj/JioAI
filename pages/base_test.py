from pages.course_page import CoursePage
from pages.course_toc_page import CourseTOC
from pages.login_page import LoginPage
from pages.news_letter import NEWSLETTER
from pages.profile_menu import ProfileMenu


class BaseTest:

    def __init__(self, driver):
        self.driver = driver
        self._login_page = LoginPage(driver)
        self._profile_menu = ProfileMenu(driver)
        self._course_page = CoursePage(driver)
        self._course_toc = CourseTOC(driver)
        self._news_letter = NEWSLETTER(driver)

    @property
    def login_page(self):
        return self._login_page

    @property
    def profile_menu(self):
        return self._profile_menu

    @property
    def course_page(self):
        return self._course_page

    @property
    def course_toc(self):
        return self._course_toc

    @property
    def news_letter(self):
        return self._news_letter
