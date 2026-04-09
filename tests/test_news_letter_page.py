import pytest

from utils.config_reader import course_completed_user, password


class TestNEWSLETTERS:
    user = course_completed_user()
    pwd = password()

    @pytest.mark.newsletter
    def test_redirection_to_news_letter_page(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        base.news_letter.redirection_to_news_letter_page()
        assert driver.current_url == "https://jiopc.embibe.com/courses/newsletter"

    @pytest.mark.newsletter
    def test_news_letter_page_title(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.news_letter_page_title()
        assert title == "Newsletter"

    @pytest.mark.newsletter
    def test_get_title_for_news_letter1(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.get_title_for_news_letter1()
        assert title == "AI-Powered Lesson Planning: From Hours to Minutes", "Title does not match expected value"

    @pytest.mark.newsletter
    def test_get_title_for_news_letter2(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.get_title_for_news_letter2()
        assert title == "Instant Feedback & Assessment with AI", "Title does not match expected value"

    @pytest.mark.newsletter
    def test_get_title_for_news_letter3(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.get_title_for_news_letter3()
        assert title == "Differentiated Instruction Made Easy with AI", "Title does not match expected value"

    @pytest.mark.newsletter
    def test_get_title_for_news_letter4(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.get_title_for_news_letter4()
        assert title == "Transform Boring Worksheets into Engaging Activities", "Title does not match expected value"

    @pytest.mark.newsletter1
    def test_get_title_for_news_letter5(self, driver, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)
        title = base.news_letter.get_title_for_news_letter5()
        assert title == "Smarter Lesson Planning with Google Gemini", "Title does not match expected value"
