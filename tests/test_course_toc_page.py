import pytest

from utils.config_reader import username, password


class TestCourseTOC:
    user = username()
    pwd = password()

    @pytest.fixture(autouse=True)
    def login(self, base):
        base.login_page.login_with_valid_password(self.user, self.pwd)

    @pytest.mark.course_toc
    def test_course_Ad_banner_is_displayed(self, base):
        base.course_toc.course_Ad_banner_is_displayed()

    @pytest.mark.course_toc
    def test_click_module_topics(self, base):
        base.course_toc.click_module_topics()

    @pytest.mark.video
    def test_click_broadcast_video(self, base):
        base.course_toc.click_broadcast_video()

    @pytest.mark.videoo
    def test_click_video2(self, base):
        base.course_toc.click_video_2()

    @pytest.mark.video
    def test_click_video3(self, base):
        base.course_toc.click_video_3()

    @pytest.mark.video
    def test_click_video4(self, base):
        base.course_toc.click_video_4()

    @pytest.mark.video
    def test_click_video5(self, base):
        base.course_toc.click_video_5()

    @pytest.mark.video
    def test_click_video6(self, base):
        base.course_toc.click_video_6()

    @pytest.mark.pdf
    def test_click_pdf1(self, base):
        base.course_toc.click_pdf1()

    @pytest.mark.pdf
    def test_click_pdf2(self, base):
        base.course_toc.click_pdf2()

