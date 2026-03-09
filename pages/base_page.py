from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger


class BasePage:
    logger = get_logger()

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_keys(self, locator, value):
        self.logger.info(f"Entering value in {locator}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(value)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

