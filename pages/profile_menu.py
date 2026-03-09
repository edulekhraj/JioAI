from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProfileMenu(BasePage):

    PROFILE_MENU_BUTTON = (By.CSS_SELECTOR, "[alt='Profile']")
    COURSE_PANEL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class='course-info-panel']>button")
    SIGN_OUT= (By.XPATH, "//div[normalize-space()='Sign out']")
    SIGN_OUT_CANCEL_BUTTON= (By.XPATH, "//button[normalize-space()='Cancel']")
    SIGN_OUT_OK_BUTTON = (By.XPATH, "//button[normalize-space()='OK']")
    BANNER = (By.CSS_SELECTOR, "[alt='Teaching Illustration']")

    MENU_OPTIONS = {
        "my_progress": (By.XPATH, "//div[text()='My Progress']"),
        "my_school": (By.XPATH, "//div[contains(text(),'My School')]"),
        "faqs": (By.XPATH, "//div[text()='FAQs']"),
        "contact_us": (By.XPATH, "//div[text()='Contact us']"),
        "feedback": (By.XPATH, "//div[text()='Feedback']"),
        "privacy_policy": (By.XPATH, "//div[contains(text(),'Privacy')]"),
        "terms_conditions": (By.XPATH, "//div[contains(text(),'Terms')]")

    }

    def open_profile_menu(self):
        self.click(self.COURSE_PANEL_CLOSE_BUTTON)
        self.click(self.PROFILE_MENU_BUTTON)

    def sign_out_menu(self):
        self.open_profile_menu()
        self.click(self.SIGN_OUT)
        self.click(self.SIGN_OUT_CANCEL_BUTTON)
        self.click(self.PROFILE_MENU_BUTTON)
        self.click(self.SIGN_OUT)
        self.click(self.SIGN_OUT_OK_BUTTON)
        self.wait_for_element_visibility(self.BANNER)

    def select_menu_option(self, option):
        self.open_profile_menu()
        self.click(self.MENU_OPTIONS[option])
