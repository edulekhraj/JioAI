import pytest

from utils.config_reader import username, password


class TestCoursePage:
    user = username()
    pwd = password()

    @pytest.fixture(autouse=True)
    def login(self, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)

    @pytest.mark.smoke
    @pytest.mark.course_page
    def test_banners_is_visible(self, base):
        banners = base.course_page.banners_are_visible()
        assert len(banners) > 0, "No banners are visible on the course page."

    @pytest.mark.course_page
    def test_my_profile_button(self, base):
        assert base.course_page.my_profile_button().is_displayed()

    @pytest.mark.smoke
    @pytest.mark.course_page
    def test_ai_foundation_course(self, base):
        assert base.course_page.ai_foundation_course().is_displayed()

    @pytest.mark.smoke
    @pytest.mark.course_page
    def test_course_title(self, base):
        title = base.course_page.course_title()
        assert title == "AI Foundation Course"

    # def test_instructor_cards(self,base):
    #     cards = base.course_page.instructor_cards()
    #     assert len(cards) > 0

    @pytest.mark.course_page
    def test_close_course_panel(self, base):
        base.course_page.close_course_panel()

    @pytest.mark.smoke
    @pytest.mark.course_page
    def test_course_navigation_page(self, base):
        course_navigation_page = base.course_page.course_navigation_page()
        assert course_navigation_page.is_displayed()
