from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NEWSLETTER(BasePage):
    GO_BACK_BUTTON = (By.CSS_SELECTOR, "[aria-label='Go back']")
    GO_TO_COURSE_PAGE = (By.CSS_SELECTOR, "[class='course-panel-enroll-button']")
    VIDEO_CLOSE_BUTTON = (By.CSS_SELECTOR, "[title='Close']")
    VIEW_NEWSLETTER = (By.XPATH, "//button[text()='View Newsletter']")
    NEWS_LETTER_TITLE = (By.CSS_SELECTOR, "[class='newsletter-title']")
    NEWS_LETTER1 = (By.XPATH, "//div[@class='newsletter-grid']/div[1]/div[2]/h3")
    NEWS_LETTER2 = (By.XPATH, "//div[@class='newsletter-grid']/div[2]/div[2]/h3")
    NEWS_LETTER3 = (By.XPATH, "//div[@class='newsletter-grid']/div[3]/div[2]/h3")
    NEWS_LETTER4 = (By.XPATH, "//div[@class='newsletter-grid']/div[4]/div[2]/h3")
    NEWS_LETTER5 = (By.XPATH, "//div[@class='newsletter-grid']/div[5]/div[2]/h3")
    NEWS_LETTER6 = (By.XPATH, "//div[@class='newsletter-grid']/div[6]/div[2]/h3")


    def redirection_to_news_letter_page(self):
        self.click(self.GO_BACK_BUTTON)
        self.click(self.GO_TO_COURSE_PAGE)
        self.click(self.VIDEO_CLOSE_BUTTON)
        self.click(self.VIEW_NEWSLETTER)

    def news_letter_page_title(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER_TITLE)
        return title

    def get_title_for_news_letter1(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER1)
        return title

    def get_title_for_news_letter2(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER2)
        return title

    def get_title_for_news_letter3(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER3)
        return title

    def get_title_for_news_letter4(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER4)
        return title

    def get_title_for_news_letter5(self):
        self.redirection_to_news_letter_page()
        title = self.get_text(self.NEWS_LETTER5)
        return title






