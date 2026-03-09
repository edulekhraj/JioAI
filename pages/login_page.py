import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME = (By.CSS_SELECTOR, "[placeholder='Enter your mobile number']")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Continue']")
    CONTINUE_WITH_OTP_BUTTON = (By.XPATH, "//span[text()='Continue with OTP']")
    SIGNIN_WITH_PASSWORD_BUTTON = (By.XPATH, "//span[text()='Sign in with Password']")
    RESET_PASSWORD = (By.XPATH, "//a[text()='Reset Password']")
    TOS = (By.XPATH, "//a[text()='Terms of Use']")
    VERIFY_OTP = (By.XPATH, "//span[text()='Verify OTP']")
    PRIVACY_POLICY = (By.XPATH, "//a[text()='Privacy Policy.']")
    Banner =(By.CSS_SELECTOR, "[alt='Teaching Illustration']")
    OTP_1 = (By.ID, "otp-0")
    # OTP_2 = (By.ID, "otp-1")
    # OTP_3 = (By.ID, "otp-2")
    # OTP_4 = (By.ID, "otp-3")
    # OTP_5 = (By.ID, "otp-4")
    # OTP_6 = (By.ID, "otp-5")


    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    # def OTP_page(self, OTP):
    #     self.send_keys(self.OTP_1, OTP[0])
    #     self.send_keys(self.OTP_2, OTP[1])
    #     self.send_keys(self.OTP_3, OTP[2])
    #     self.send_keys(self.OTP_4, OTP[3])
    #     self.send_keys(self.OTP_5, OTP[4])
    #     self.send_keys(self.OTP_6, OTP[5])

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_sign_in_with_password(self):
        self.click(self.SIGNIN_WITH_PASSWORD_BUTTON)

    def click_sign_in_with_OTP(self):
        self.click(self.CONTINUE_WITH_OTP_BUTTON)

    def Sign_in_with_OTP(self):
        self.click(self.Sign_in_with_OTP())

    def login_with_valid_password(self, username, password):
        self.enter_username(username)
        time.sleep(2)
        self.click_sign_in_with_password()
        self.enter_password(password)
        self.click_login()
        time.sleep(5)

    def login_with_invalid_password(self, username, password):
        self.enter_username(username)
        time.sleep(2)
        self.click_sign_in_with_password()
        self.enter_password(password)
        self.click_login()
        time.sleep(5)
    def terms_of_use(self):
        self.click(self.TOS)

    def privacy_policy(self):
        self.click(self.PRIVACY_POLICY)

    def login_wit_OTP(self, username, OTP):
        OTP = str(OTP)
        self.enter_username(username)
        time.sleep(2)
        self.click(self.CONTINUE_WITH_OTP_BUTTON)
        time.sleep(2)
        self.send_keys(self.OTP_1, OTP)
        time.sleep(5)
        self.click(self.VERIFY_OTP)
        time.sleep(5)

    def banner_in_login_page(self):
       assert self.driver.find_element(*self.Banner).is_displayed()

