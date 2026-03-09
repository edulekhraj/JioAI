import time

import pytest
from selenium.webdriver.common.by import By
from utils.config_reader import username, password


class TestLoginPage:
    user = username()
    pwd = password()

    @pytest.mark.smoke
    def test_valid_login(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        assert 'select-book' in driver.current_url

    @pytest.mark.smoke
    def test_invalid_login(self, driver, base):
        base.login_page.login_with_invalid_password(self.user, "Embibe@12345")
        time.sleep(3)
        assert 'login' in driver.current_url

    @pytest.mark.smoke
    def test_tos(self, driver, base):
        base.login_page.terms_of_use()
        driver.switch_to.window(driver.window_handles[1])
        assert 'terms-conditions' in driver.current_url
        assert 'grievance.officer@jio.com' in driver.page_source
        time.sleep(5)  # wait added purposefully to view the page in UI

    @pytest.mark.smoke
    def test_privacy_policy(self, driver, base):
        base.login_page.privacy_policy()
        driver.switch_to.window(driver.window_handles[1])
        assert 'AI Classroom – Privacy Policy' in driver.title
        assert 'grievance.officer@jio.com' in driver.page_source
        time.sleep(5)  # wait added purposefully to view the page in UI

    @pytest.mark.smoke
    def test_OTP_login(self, driver, base):
        base.login_page.login_wit_OTP(8660301503, 123456)
        assert driver.find_element(By.CSS_SELECTOR, "[class='sc-cZsuCz ijcQcq']").is_displayed()
        time.sleep(5)  # wait added purposefully to view the page in UI

    @pytest.mark.smoke
    def test_banner_in_login_page(self, base):
        base.login_page.banner_in_login_page()

