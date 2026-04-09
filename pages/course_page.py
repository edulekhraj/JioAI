import time

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CoursePage(BasePage):
    BANNERS = (By.XPATH, "//div[@class='ad-carousel-track']/div")
    MY_PROFILE_BUTTON = (By.CSS_SELECTOR, "[alt='Profile']")
    MY_PROGRESS = (By.XPATH, "//div[text()='My Progress']")
    COURSE_TITLE = (By.CSS_SELECTOR, "[class='course-title']")
    INSTRUCTOR_CARDS = (By.XPATH, "//div[@class='instructor-card ']")
    CLOSE_COURSE_PANEL = (By.CSS_SELECTOR, "[class='course-panel-close-btn']")
    GO_TO_COURSE_PAGE = (By.XPATH, "//div[text()='Go to Course Page']")
    COURSE_INFO_PANEL = (By.CSS_SELECTOR, "[class='course-info-panel']")
    COURSE_AD_BANNER = (By.CSS_SELECTOR, "[class='ad-container']")

    def banners_are_visible(self):
        time.sleep(3)  # Wait for banners to load
        # self.click(self.CLOSE_COURSE_PANEL)
        banners = self.driver.find_elements(*self.BANNERS)
        return banners

    def my_profile_button(self):
        self.click(self.CLOSE_COURSE_PANEL)
        return self.wait_for_element_visibility(self.MY_PROFILE_BUTTON)

    def ai_foundation_course(self):
        return self.wait_for_element_visibility(self.COURSE_INFO_PANEL)

    def course_title(self):
        return self.get_text(self.COURSE_TITLE)

    def instructor_cards(self):
        return self.driver.find_elements(*self.INSTRUCTOR_CARDS)

    def close_course_panel(self):
        self.click(self.CLOSE_COURSE_PANEL)

    def course_navigation_page(self):
        self.click(self.GO_TO_COURSE_PAGE)
        self.wait_for_element_visibility(self.COURSE_AD_BANNER)
        return self.driver.find_element(*self.COURSE_AD_BANNER)
