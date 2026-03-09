import time

import pytest

from utils.config_reader import username, password


class TestProfileMenu:
    user = username()
    pwd = password()

    @pytest.fixture(autouse=True)
    def login(self, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_open_profile_menu(self, driver, base):
        base.profile_menu.open_profile_menu()
        assert 'https://jiopc.embibe.com/courses/select-book' in driver.current_url
        time.sleep(3)  # wait added purposefully to view the profile menu in UI

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_my_progress(self,driver, base):
        base.profile_menu.select_menu_option("my_progress")
        time.sleep(3)
        assert 'my-progress' in driver.current_url

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_my_school(self,driver, base):
        base.profile_menu.select_menu_option("my_school")
        time.sleep(3)
        assert 'my-school-details' in driver.current_url

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_faqs(self,driver, base):
        base.profile_menu.select_menu_option("faqs")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        assert 'support' in driver.current_url

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_contact_us(self, driver, base):
        base.profile_menu.select_menu_option("contact_us")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        assert 'feedback' in driver.current_url

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_feedback(self,driver, base):
        base.profile_menu.select_menu_option("feedback")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        assert 'feedback' in driver.current_url

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_privacy_policy(self,driver, base):
        base.profile_menu.select_menu_option("privacy_policy")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        assert 'policy' in driver.current_url
        assert 'grievance.officer@jio.com' in base.driver.page_source

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_terms_conditions(self,driver, base):
        base.profile_menu.select_menu_option("terms_conditions")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        assert 'terms' in driver.current_url
        assert 'grievance.officer@jio.com' in base.driver.page_source

    @pytest.mark.smoke
    @pytest.mark.profile_menu
    def test_click_sign_out(self,driver, base):
        base.profile_menu.sign_out_menu()
        assert 'login' in driver.current_url

