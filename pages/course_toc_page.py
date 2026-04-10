import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class CourseTOC(BasePage):
    VIDEO_CLS_BTN = (By.CSS_SELECTOR, "[title='Close']")
    COURSE_AD_BANNER = (By.CSS_SELECTOR, "[class='ad-container']")
    GO_TO_COURSE_PAGE = (By.XPATH, "//div[text()='Go to Course Page']")
    RESUME_POPUP = (By.XPATH, "//div[text()='Continue from where you left?']")
    RESUME_NO_BUTTON = (By.XPATH, "//button[text()='No']")
    RESUME_YES_BUTTON = (By.XPATH, "//button[text()='Yes']")
    VIDEO2 = (By.XPATH, "//div[@class='spoilers']/div[1]/div[2]/div[1]/div[1]/div[2]")
    VIDEO3 = (By.XPATH, "//div[@class='spoilers']/div[1]/div[2]/div[1]/div[1]/div[3]")
    VIDEO4 = (By.XPATH, "//div[@class='spoilers']/div[1]/div[2]/div[1]/div[1]/div[4]")
    VIDEO5 = (By.XPATH, "//div[@class='spoilers']/div[1]/div[2]/div[1]/div[1]/div[5]")
    VIDEO6 = (By.XPATH, "//div[@class='spoilers']/div[1]/div[2]/div[1]/div[1]/div[6]")
    PDF1 = (By.XPATH, "//div[@class='spoilers']/div[2]/div[2]/div/div[1]/div[1]")
    PDF2 = (By.XPATH, "//div[@class='spoilers']/div[2]/div[2]/div/div[1]/div[2]")
    LANG_OKAY_BTN = (By.CSS_SELECTOR, "[type='button']")

    # MODULE_LIST = (By.XPATH, "//div[text()='Module']/parent::div/div[2]/div")

    def course_Ad_banner_is_displayed(self):
        self.click(self.GO_TO_COURSE_PAGE)
        time.sleep(10)
        return self.wait_for_element_visibility(self.COURSE_AD_BANNER)

    def verify_video_playback(self):

        time1 = self.driver.find_element(By.CSS_SELECTOR, ".current-time").text

        time.sleep(5)

        time2 = self.driver.find_element(By.CSS_SELECTOR, ".current-time").text

        assert time1 != time2, "Video did not start playing"

    def resume_video_popup(self):
        try:
            self.driver.find_element(*self.RESUME_POPUP).is_displayed()
            self.click(self.RESUME_NO_BUTTON)

        except NoSuchElementException:
            pass

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(5)

    def click_module_topics(self):
        self.click(self.GO_TO_COURSE_PAGE)
        time.sleep(5)
        self.click(self.VIDEO_CLS_BTN)
        self.click(self.LANG_OKAY_BTN)
        self.click(self.driver.find_element(By.CSS_SELECTOR, "[class='submit-btn ']"))
        time.sleep(10)

    def click_broadcast_video(self):
        self.click_module_topics()
        self.resume_video_popup()

    def click_video_2(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.VIDEO2)
        self.click(self.RESUME_YES_BUTTON)
        self.click(self.RESUME_YES_BUTTON)
        self.resume_video_popup()
        # self.verify_video_playback()

    def click_video_3(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.VIDEO3)
        self.click(self.RESUME_YES_BUTTON)
        self.resume_video_popup()

    def click_video_4(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.VIDEO4)
        self.click(self.RESUME_YES_BUTTON)
        self.resume_video_popup()

    def click_video_5(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.VIDEO5)
        self.click(self.RESUME_YES_BUTTON)
        self.resume_video_popup()

    def click_video_6(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.VIDEO6)
        self.click(self.RESUME_YES_BUTTON)
        self.resume_video_popup()

    def click_pdf1(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.PDF1)
        self.click(self.RESUME_YES_BUTTON)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Download PDF']").is_displayed()

    def click_pdf2(self):
        self.click_module_topics()
        self.resume_video_popup()
        self.click(self.PDF2)
        self.click(self.RESUME_YES_BUTTON)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Download PDF']").is_displayed()

